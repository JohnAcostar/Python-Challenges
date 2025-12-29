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

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit):
    """
    Ordena un single_linked_list usando Selection Sort
    """
    n = my_list["size"]
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if sort_crit(get_element(my_list, j), get_element(my_list, min_index)):
                min_index = j
        if min_index != i:
            exchange(my_list, i, min_index)
    return my_list


def insertion_sort(my_list, sort_crit):
    """
    Ordena un single_linked_list usando Insertion Sort
    """
    n = my_list["size"]
    for i in range(1, n):
        key = get_element(my_list, i)
        j = i - 1
        while j >= 0 and not sort_crit(get_element(my_list, j), key):
            change_info(my_list, j + 1, get_element(my_list, j))
            j -= 1
        change_info(my_list, j + 1, key)
    return my_list


def shell_sort(my_list, sort_crit):
    """
    Ordena un single_linked_list usando shell sort :P
    """
    n = my_list["size"]
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = get_element(my_list, i)
            j = i
            while j >= gap and not sort_crit(get_element(my_list, j - gap), temp):
                change_info(my_list, j, get_element(my_list, j - gap))
                j -= gap
            change_info(my_list, j, temp)
        gap //= 2
    return my_list


def merge(l1, l2, sort_crit):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada, single_linked_list.
    """
    result = new_list()
    i, j = 0, 0

    while i < l1["size"] and j < l2["size"]:
        if sort_crit(get_element(l1,i), get_element(l2,j)):
            add_last(result, get_element(l1,i))
            i += 1
        else:
            add_last(result, get_element(l2,j))
            j += 1

    while i < l1["size"]:
        add_last(result, get_element(l1,i))
        i += 1

    while j < l2["size"]:
        add_last(result, get_element(l2,j))
        j += 1

    return result

def merge_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo recursivo de ordenamiento Merge Sort.

    Se divide la lista en dos partes iguales* y se ordenan de forma recursiva. Luego se mezclan las dos partes ordenadas.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.
    """
    if my_list["size"] <= 1:
        return my_list  
    
    mid = my_list["size"] // 2
    left_half = sub_list(my_list, 0, mid)
    right_half = sub_list(my_list, mid, my_list["size"] - mid)

    left_sorted = merge_sort(left_half, sort_crit)
    right_sorted = merge_sort(right_half, sort_crit)

    return merge(left_sorted, right_sorted, sort_crit)
    
def quick_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list

    # Encontrar el primer elemento de la lista para verlo como pivote
    pivot = first_element(my_list)

    # Crear listas auxiliares 
    less = new_list()
    equal = new_list()
    greater = new_list()

    # Recorrer Toda la lista nodo por nodo segun el pivote
    node = my_list["first"]
    while node is not None:
        element = node["info"]
        if sort_crit(element, pivot) and not sort_crit(pivot, element):
            add_last(less, element)
        elif sort_crit(pivot, element) and not sort_crit(element, pivot):
            add_last(greater, element)
        else:
            add_last(equal, element)
        node = node["next"]

    # Recursión de lado izquierdo y derecho
    less_sorted = quick_sort(less, sort_crit) if size(less) > 1 else less
    greater_sorted = quick_sort(greater, sort_crit) if size(greater) > 1 else greater

    # Poner en blanco la lista original
    my_list["first"] = None
    my_list["last"] = None
    my_list["size"] = 0

    # Reconstruir con las sublistas ordenadas
    node = less_sorted["first"]
    while node is not None:
        add_last(my_list, node["info"])
        node = node["next"]

    node = equal["first"]
    while node is not None:
        add_last(my_list, node["info"])
        node = node["next"]

    node = greater_sorted["first"]
    while node is not None:
        add_last(my_list, node["info"])
        node = node["next"]

    return my_list