from socketio.exceptions import ConnectionError
from kvdb.flags import parse_cli_args
import socketio
import time
from kvdb.config import *
from kvdb.server.exceptions import (
    KVDBError,
    BadArityError,
    NoCommandError,
    NoCommandProvidedError,
    NoParamsProvidedError,
    NoCommandTemplateError
)

from kvdb.server.mapper import command_template_table


def response_to_stdout(*args):
    res = args[0]
    err = args[1]
    msg = res if not err else err
    print(">", msg)


def main():
    # args = parse_cli_args()
    print("kvdb-cli started :))")
    host = HOST
    port = PORT
    # command = args.command
    # op = command[0]
    # params = command[1:]
    while(True):

        try:
            command_template = input("")
            if(command_template not in command_template_table):
                raise NoCommandTemplateError(command_template)

            command_template_op = command_template.split(" ")[1]
            command_instance = input("")
            op = command_instance.split(" ")[0]
            params = command_instance.split(" ")[1:]

            if(op == "#"):
                raise NoCommandError(command_instance)
            
            if(command_template == "# exit"):
                if(op == "exit"):
                    break
                else:
                    raise NoCommandError(command_instance)

            try:
                client = socketio.Client()
                client.connect(f'ws://{host}:{port}')
                client.emit('kvdb:command', {
                            'template_op':command_template_op ,'cmd': op, 'params': params}, callback=response_to_stdout)
                time.sleep(0.5)
                client.disconnect()

            except KVDBError as e:
                print(str(e))

            except ConnectionError:
                print(f'Unable to connect to host {host} on port {port}')
                exit(0)

        except (NoCommandError, NoCommandTemplateError) as e:
            print(str(e))


if __name__ == '__main__':
    main()
