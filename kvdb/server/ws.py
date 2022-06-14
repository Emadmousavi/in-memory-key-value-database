import socketio
import os
import geventwebsocket as geventws
from kvdb.server.mapper import command_table
from kvdb.store import KVStore
from kvdb.flags import parse_server_args
from kvdb.server.exceptions import (
    KVDBError,
    BadArityError,
    NoCommandError,
    NoCommandProvidedError,
    NoParamsProvidedError,
    NoTemplateProvidedError,
    NoCommandTemplateError,
    NotMatchWithTemplateError,
)


class KVDBSockServer(socketio.Server):
    def __init__(self, data_store: KVStore, data_store_name: str):
        super().__init__(async_mode='gevent')
        self.__kv_stores = {}
        self.on('connect', self.client_connected)
        self.on('disconnect', self.client_disconnected)
        self.on('kvdb:command', self.handle_kvdb_command)

        args = parse_server_args()
        self.stores_dir = args.kv_dir

        self.init_kv_stores()
        
        # remove format from data_store_name
        data_store_name = data_store_name.split(".")[0]
        
        # set default store
        self.__kv_store = self.__kv_stores[data_store_name]

    def init_kv_stores(self):
        for filename in os.listdir(self.stores_dir):
            file_full_path = os.path.join(self.stores_dir, filename)
            if os.path.isfile(file_full_path):
                file_name_without_format = filename.split('.')[0]
                self.add_store(file_name_without_format)

    def listen(self, host: str, port: int):
        server = geventws.WebSocketServer((host, port), socketio.WSGIApp(self))
        print(f'Server listening @ {host} on port {port}')
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Server shutting down')
            server.close()
            exit(0)

    def add_store(self, store_name: str):
        kv_source = os.path.join(self.stores_dir, f'{store_name}.kv')
        new_store = KVStore(self.stores_dir, kv_source)
        self.__kv_stores[store_name] = new_store
        return self.__kv_stores[store_name]

    def switch_store(self, store_name: str):
        new_store = None
        if store_name not in self.__kv_stores:
            new_store = self.add_store(store_name)
        else:
            new_store = self.__kv_stores[store_name]

        self.__kv_store = new_store

    def list_stores(self):
        stores_name = []
        for store in self.__kv_stores:
            stores_name.append(store)

        return stores_name

    def client_connected(self, sid, environ):
        print(f'Client {sid} connected')

    def client_disconnected(self, sid):
        print(f'Client {sid} disconnected')

    def load_data_from_file_to_db(self, file_path: str, store_name: str):
        try:
            db = self.__kv_stores[store_name]
            db.load_data_from_file_to_store(file_path)
        except KeyError as e:
            return f"db with name '{store_name}' not found"

    def dump_db_on_file(self, store_name: str, file_path: str):
        try:
            db = self.__kv_stores[store_name]
            print("self: ",self.__kv_store.prinkv())
            print("db: ",db.prinkv())
            db.dump_store_on_file(file_path)
            
        except KeyError as e:
            return f"db with name '{store_name}' not found"
        
    def handle_kvdb_command(self, sid, data):

        try:
            if 'cmd' not in data:
                raise NoCommandProvidedError

            if 'params' not in data:
                raise NoParamsProvidedError

            if 'template_op' not in data:
                raise NoTemplateProvidedError

            template_op = data['template_op']
            cmd = data['cmd']
            params = data['params']

            print(template_op, cmd)

            if(template_op != cmd):
                raise NotMatchWithTemplateError(cmd, template_op)

            cmd_handler, arity = command_table.get(cmd, (None, None))

            if not cmd_handler:
                raise NoCommandError(cmd)

            plen = len(params)
            if plen != arity:
                raise BadArityError(cmd, plen, arity)

            if(cmd == "use"):
                if(params[0].replace(" ", "") == ""):
                    return (None, "db name can not be empty")
                else:
                    return (cmd_handler(params, self), None)

            if(cmd in ["list", "use", "load", "dump"]):

                if(cmd == "use" and params[0].replace(" ", "") == ""):
                    return (None, "db name can not be empty")

                return (cmd_handler(params, self), None)
            else:
                return (cmd_handler(params, self.__kv_store), None)

        except KVDBError as e:
            return (None, str(e))
