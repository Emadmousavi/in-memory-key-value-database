from kvdb.server.handlers import *

command_table = {
    'get': (handle_get_key, 1), 
    'set': (handle_set_key, 2), 
    'del': (handle_del_key, 1), 
    'count': (handle_count_keys, 0),
    'ping': (handle_ping_client, 0),
    'keys': (handle_match_keys, 1),
    'clear': (handle_clear_keys, 0),
    'use': (handle_use_db, 1),
    'list': (handle_list_dbs, 0),
    'load': (handle_load_data_from_file_to_db,2),
    'dump': (handle_dump_db_on_file,2),
}

command_template_table = [
    "# exit",
    "# set key value",
    "# get key",
    "# del key",
    "# keys regex",
    "# use db_name",
    "# list",
    "# dump db_name path",
    "# load path db_name",
    "# count",
    "# ping",
    "# clear"
]