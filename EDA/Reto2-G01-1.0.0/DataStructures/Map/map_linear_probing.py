import random as rd

from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me

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
            'table': al.new_list(),  # Lista vacía para entradas
            'current_factor': 0,
            'limit_factor': load_factor,
            'size': 0,
            'type': 'PROBE_HASH_MAP'
        }

        # Inicializar la tabla con entradas vacías
        for _ in range(capacity):
            entry = me.new_map_entry(None, None)
            al.add_last(hash_table['table'], entry)

        return hash_table

    except Exception as exp:
        
        raise RuntimeError(f'Probe:newMap -> {exp}')

def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False


def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def rehash(my_map):
    new_capacity = mp.next_prime(2 * my_map["capacity"])
    new_hash_map = new_map(new_capacity, my_map["limit_factor"], my_map["prime"])

    for i in range(al.size(my_map["table"])):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        value = me.get_value(entry)

        if key is not None and key != "__EMPTY__":
            hash_value = mp.hash_value(new_hash_map, key)
            _, pos = find_slot(new_hash_map, key, hash_value)
            al.change_info(new_hash_map["table"], pos, me.new_map_entry(key, value))
            new_hash_map["size"] += 1

    new_hash_map["current_factor"] = new_hash_map["size"] / new_hash_map["capacity"]

    my_map.clear()
    my_map.update(new_hash_map)

    return my_map
    
def put(my_map, key, value):
    """
    Agrega una nueva entrada llave-valor a la tabla de hash. Si la llave ya existe en la tabla, se actualiza el value de la entrada.
    """
    try:
        # Calcular el hash inicial
        capacity = my_map["capacity"]
        hash_value = mp.hash_value(my_map,key)

        # Buscar el slot adecuado
        occupied, pos = find_slot(my_map, key, hash_value)

        # Crear o actualizar entrada
        if occupied:
            # Actualizar value de la key existente
            entry = al.get_element(my_map["table"], pos)
            me.set_value(entry, value)
        else:
            # Insertar nueva entrada
            entry = me.new_map_entry(key, value)
            al.change_info(my_map["table"], pos, entry)
            my_map["size"] += 1
            my_map["current_factor"] = my_map["size"] / capacity

        # Rehash si se supera el factor de carga
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)

        return my_map

    except Exception as exp:
        raise RuntimeError(f'Probe:put -> {exp}')
    
def contains(my_map, key):
    """
    Valida si una llave dada se encuentra en la tabla de simbolos.
    """
    try:
        if my_map["size"] == 0:
            return False

        hash_value = mp.hash_value(my_map, key)

        # Buscar slot adecuado
        occupied, pos = find_slot(my_map, key, hash_value)

        # Si el slot estaba ocupado por la key buscada, existe
        return occupied

    except Exception as exp:
        raise RuntimeError(f'Probe:contains -> {exp}')
    
def get(my_map, key):
    """
    Obtiene el valor asociado a una llave dada en la tabla de simbolos.

    """
    try:
        if my_map["size"] == 0:
            return None

        # Calcular posición inicial usando hash
        hash_value = mp.hash_value(my_map,key)

        # Buscar slot
        occupied, pos = find_slot(my_map, key, hash_value)

        if occupied:
            entry = al.get_element(my_map["table"], pos)
            return me.get_value(entry)
        else:
            return None

    except Exception as exp:
        raise RuntimeError(f'Probe:get -> {exp}')
    
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mp

def remove(my_map, key):
    """
    Elimina una entrada llave-valor de la tabla de símbolos asociada a una llave dada. 
    La entrada eliminada debe reemplazarse por la entrada llave-valor 
    """
    try:
        if my_map["size"] == 0:
            return my_map  # Nada que eliminar

        # Calcular posición inicial usando hash
        prime = my_map["prime"]
        scale = my_map["scale"]
        shift = my_map["shift"]
        capacity = my_map["capacity"]
        hash_value = ((hash(key) * scale + shift) % prime) % capacity

        # Buscar slot
        occupied, pos = find_slot(my_map, key, hash_value)

        if occupied:
            
            empty_entry = me.new_map_entry("__EMPTY__", "__EMPTY__")
            al.change_info(my_map["table"], pos, empty_entry)
            my_map["size"] -= 1

        return my_map

    except Exception as exp:
        raise RuntimeError(f'Probe:remove -> {exp}')
    
def size(my_map):
    '''Valida si la tabla de simbolos está vacía.'''
    return my_map["size"]

def is_empty(my_map):
    """Valida si la tabla de simbolos está vacía. """
    
    return my_map["size"] == 0

def key_set(my_map):
    """Obtiene la lista de llaves de la tabla de simbolos."""
    lista = al.new_list()
    table = my_map["table"]
    for i in range(0,al.size(table)):
        entry = al.get_element(table, i)
        key = me.get_key(entry)
        
        if key is not None and key != "__EMPTY__":
            al.add_last(lista, key)

    return lista
    


def value_set(my_map):
    """Obtiene la lista de valores de la tabla de simbolos."""
    lista = al.new_list()
    table = my_map["table"]
    for i in range(0,al.size(table)):
        entry = al.get_element(table, i)
        value = me.get_value(entry)
        
        if value is not None and value != "__EMPTY__":
            al.add_last(lista, value)

    return lista


