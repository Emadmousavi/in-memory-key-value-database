from kvdb.server.ws import KVDBSockServer
from kvdb.store import KVStore
from kvdb.flags import parse_server_args
import os
from environs import Env

def main():
    
    args = parse_server_args()
    
    host = args.host
    port = args.port
    kv_dir = args.kv_dir
    kv_source = args.kv_src
    _ , kv_name = os.path.split(kv_source)

    socket_server = KVDBSockServer(KVStore(kv_dir, kv_source),kv_name)
    socket_server.listen(host, port)


if __name__ == '__main__':
    main()