import os
from typing import List, Dict
from kvdb.store import KVStore
import re 

def handle_ping_client(params: List[str], store: KVStore) -> str:
    return 'PONG'

def handle_get_key(params: List[str], store: KVStore) -> any:
    k = params[0]
    v = store.getk(k)
    return v if v != None else '<None>'

def handle_set_key(params: List[str], store: KVStore) -> str:
    k = params[0]
    v = params[1]
    store.setk(k,v)
    return 'OK'

def handle_del_key(params: List[str], store: KVStore) -> str:
    k = params[0]
    store.delk(k)
    return 'OK'

def handle_count_keys(params: List[str], store: KVStore) -> int:
    return store.countk()
 
def handle_match_keys(params: List[str], store: KVStore) -> Dict[str, str]:
    p = params[0]
    return list(filter(lambda k: re.match(p, k), store.getk()))

def handle_clear_keys(params: List[str], store: KVStore) -> str:
    store.cleark()
    return 'OK'

def handle_use_db(params: List[str], store) -> str:
    store_name = params[0]
    store.switch_store(store_name)
    return 'OK'

def handle_list_dbs(params: List[str], store) -> list:
    return store.list_stores()

def handle_load_data_from_file_to_db(params: List[str],store):
    file_path = params[0]
    store_name = params[1]
    
    if(file_path.split("/")[0] == '.'):
        path_arr = file_path.split("/")
        path_arr[0] = os.getcwd()
        file_path = r"/".join(path_arr)
        print(file_path)
    response = store.load_data_from_file_to_db(file_path, store_name)
    if(response):
        return response
    return 'OK'

def handle_dump_db_on_file(params: List[str], store):
    store_name = params[0]
    file_path = params[1]
    
    if(file_path.split("/")[0] == '.'):
        path_arr = file_path.split("/")
        path_arr[0] = os.getcwd()
        file_path = r"/".join(path_arr)
        print(file_path)
    response = store.dump_db_on_file(store_name, file_path)
    if(response):
        return response
    return 'OK'