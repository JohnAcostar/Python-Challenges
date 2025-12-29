import random as rd

from DataStructures.List import array_list as lt
from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as slt

def new_map(num_elements, load_factor, prime=109345121):
    try:
        capacity = mp.next_prime(int(num_elements / load_factor))
        scale = 1
        shift = 0

        hash_table = {
            'prime': prime,
            'capacity': capacity,
            'scale': scale,
            'shift': shift,
            'table': lt.new_list(),  # Lista vacía para entradas
            'current_factor': 0,
            'limit_factor': load_factor,
            'size': 0,
        }

        # Inicializar la tabla con entradas vacías
        for _ in range(capacity):
            entry = slt.new_list()
            lt.add_last(hash_table['table'], entry)

        return hash_table

    except Exception as exp:
        
        raise RuntimeError(f'Probe:newMap -> {exp}')
    

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def rehash(my_map):
    new_capacity = mp.next_prime(2 * my_map["capacity"])

    new_map_data = new_map(new_capacity, my_map["limit_factor"], my_map["prime"])

    for i in range(lt.size(my_map["table"])):
        bucket = lt.get_element(my_map["table"], i)
        for j in range(slt.size(bucket)):
            entry = slt.get_element(bucket, j)
            key = me.get_key(entry)
            value = me.get_value(entry)
            if key is not None:
                hash_val = mp.hash_value(new_map_data, key)
                new_bucket = lt.get_element(new_map_data["table"], hash_val)
                slt.add_last(new_bucket, me.new_map_entry(key, value))
                new_map_data["size"] += 1

    my_map["table"] = new_map_data["table"]
    my_map["capacity"] = new_map_data["capacity"]
    my_map["size"] = new_map_data["size"]
    my_map["prime"] = new_map_data["prime"]
    my_map["scale"] = new_map_data["scale"]
    my_map["shift"] = new_map_data["shift"]
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map
    

def put(my_map, key, value):
    
    hasheado = mp.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hasheado)
    
    pos = slt.is_present(bucket, key, default_compare)
    
    if pos > -1:
        entry = slt.get_element(bucket, pos)
        me.set_value(entry, value)
    
    else:
        entry = me.new_map_entry(key, value)
        slt.add_last(bucket, entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)
        
    return my_map

def contains(my_map, key):
    hasheado = mp.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hasheado)
    pos = slt.is_present(bucket, key, default_compare)
    return pos > -1

def get(my_map, key):
    hasheado = mp.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hasheado)
    pos = slt.is_present(bucket, key, default_compare)
    if pos > -1:
        entry = slt.get_element(bucket, pos)
        return me.get_value(entry)
    return None

def remove(my_map, key):
    hasheado = mp.hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hasheado)
    pos = slt.is_present(bucket, key, default_compare)
    if pos > -1:
        elem = slt.get_element(bucket, pos)
        slt.delete_element(bucket, pos)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        return me.get_value(elem)
    return None

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    lista = lt.new_list()
    for i in range(0,lt.size(my_map["table"])):
        bucket = lt.get_element(my_map["table"], i)
        for j in range(0,slt.size(bucket)):
            entry = slt.get_element(bucket, j)
            if me.get_key(entry) is not None:
                lt.add_last(lista, me.get_key(entry))
                
    return lista


def value_set(my_map):
    lista = lt.new_list()
    for i in range(0,lt.size(my_map["table"])):
        bucket = lt.get_element(my_map["table"], i)
        for j in range(0,slt.size(bucket)):
            entry = slt.get_element(bucket, j)
            if me.get_key(entry) is not None:
                lt.add_last(lista, me.get_value(entry))
                
    return lista