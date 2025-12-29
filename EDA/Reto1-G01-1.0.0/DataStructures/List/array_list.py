def new_list():
    """
    Crea una nueva lista basada en un arreglo de Python (list).
    """
    newlist = {"elements": [], "size": 0,}
    return newlist

def get_element(my_list, pos): #Esta función se desarollo como se muestra en la documentación de
                               #isis1225devs.github.io, en la que se especifica el caso que el pos esta por fuera del size
                            
    """
    Retorna el elemento en la posición pos (0-based).
    """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    return my_list["elements"][pos]

#Función que se pasa en el laboratorio
def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista.
    """
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista.
    """
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def is_empty(my_list):
    """
    Retorna True si la lista está vacía.
    """
    return my_list["size"] == 0


def size(my_list):
    """
    Retorna el número de elementos en la lista.
    """
    return my_list["size"]


def first_element(my_list):
    """
    Retorna el primer elemento de la lista.
    """
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][0]


def last_element(my_list):
    """
    Retorna el último elemento de la lista.
    """
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][-1]

def remove_first(my_list):
    """
    Elimina el primer elemento de la lista.
    """
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    
    element = my_list["elements"].pop(0)
    my_list["size"] -= 1
    return element

def remove_last(my_list):
    """
    Elimina el último elemento de la lista y lo retorna.
    """
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    element = my_list["elements"].pop()
    my_list["size"] -= 1
    return element

def insert_element(my_list, element, pos):
    """
    Inserta un elemento en la posición indicada.
    """
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    """
    Elimina el elemento en la posición indicada.
    """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    """
    Cambia la información en la posición indicada.
    """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    """
    Intercambia los elementos en pos1 y pos2.
    """
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list


def sub_list(my_list, pos, num_elements):
    """
    Retorna una sublista a partir de pos.
    """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    end = min(pos + num_elements, my_list["size"])
    sub = {
        "elements": my_list["elements"][pos:end],
        "size": end - pos
    }
    return sub

    
    