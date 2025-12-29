def new_list():
    """
    Crea una nueva lista simplemente enlazada vacía.
    """
    newlist = {"first": None, 
               "last": None, 
               "size": 0,
    }
    return newlist

#Funcion que se usa en la guia del laboratorio
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def get_element(my_list, pos): #Esta función se desarollo como se muestra en la documentación de
                               #isis1225devs.github.io, en la que se especifica el caso que el pos esta por fuera del size
    """
    Retorna el elemento en la posición pos (0-based).
    """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")

    current = my_list["first"]
    idx = 0
    while idx < pos:
        current = current["next"]
        idx += 1
    return current["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    """
    Agrega un elemento al inicio de la lista enlazada.
    """
    new_node = {"info": element, "next": my_list["first"]}
    my_list["first"] = new_node
    if my_list["last"] is None:  # lista estaba vacía
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    """
    Agrega un elemento al final de la lista enlazada.
    """
    new_node = {"info": element, "next": None}
    if my_list["first"] is None:  # lista vacía
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list


def is_empty(my_list):
    """
    Retorna True si la lista está vacía.
    """
    return my_list["size"] == 0


def size(my_list):
    """
    Retorna el número de elementos en la lista enlazada.
    """
    return my_list["size"]


def first_element(my_list):
    """
    Retorna el primer elemento de la lista.
    """
    if my_list["first"] is None:
        raise IndexError("list index out of range")
    return my_list["first"]["info"]


def last_element(my_list):
    """
    Retorna el último elemento de la lista.
    """
    if my_list["last"] is None:
        raise IndexError("list index out of range")
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    """remover un elemento """
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["first"] is None:
            my_list["last"] = None
        my_list["size"] -= 1
        return my_list

    prev = my_list["first"]
    idx = 0
    while idx < pos - 1:
        prev = prev["next"]
        idx += 1

    node_to_delete = prev["next"]
    prev["next"] = node_to_delete["next"]

    if node_to_delete == my_list["last"]:
        my_list["last"] = prev

    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    """remover el primer elemento"""
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")

    value = my_list["first"]["info"]

    my_list["first"] = my_list["first"]["next"]

    if my_list["first"] is None:
        my_list["last"] = None

    my_list["size"] -= 1

    return value

def remove_last(my_list):
    """remover el ultimo elemento"""

    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    
    if my_list["size"] == 1:
        value = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return value

    prev = my_list["first"]
    while prev["next"] is not my_list["last"]:
        prev = prev["next"]

    value = my_list["last"]["info"]

    prev["next"] = None
    my_list["last"] = prev
    my_list["size"] -= 1

    return value

def insert_element(my_list,element,pos):
    """Insertar un elemento"""
    
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        new_node = {"info": element, "next": my_list["first"]}
        my_list["first"] = new_node
        if my_list["first"] is None:
            my_list["last"] = new_node
        my_list["size"] += 1
        return my_list

    prev = my_list["first"]
    for x in range(pos - 1):
        prev = prev["next"]

    new_node = {"info": element, "next": prev["next"]}
    prev["next"] = new_node

    if new_node["next"] is None:
        my_list["last"] = new_node

    my_list["size"] += 1
    return my_list
    
def change_info(my_list, pos, new_info):
    """
    Cambia la información de un elemento en la posición dada.
    """
    
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")

    current = my_list["first"]
    idx = 0
    while idx < pos:
        current = current["next"]
        idx += 1

    current["info"] = new_info

    return my_list

def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de dos nodos.
    """
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise Exception("IndexError: list index out of range")

    if pos_1 == pos_2:
        return my_list  

    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1

    current = my_list["first"]
    idx = 0
    node1 = node2 = None

    for x in range(my_list["size"]):
        if idx == pos_1:
            node1 = current
        if idx == pos_2:
            node2 = current
            break
        current = current["next"]
        idx += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]

    return my_list

def sub_list(my_list, pos, num_elements):
    """
    Retorna una sublista de my_list.
    """
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")

    actual = my_list["first"]
    idx = 0
    while idx < pos:
        actual = actual["next"]
        idx += 1

    sublist = {"size": 0, "first": None, "last": None}
    count = 0
    while actual is not None and count < num_elements:
        new_node = {"info": actual["info"], "next": None}
        if sublist["first"] is None:
            sublist["first"] = new_node
            sublist["last"] = new_node
        else:
            sublist["last"]["next"] = new_node
            sublist["last"] = new_node
        sublist["size"] += 1
        count += 1
        actual = actual["next"]

    return sublist