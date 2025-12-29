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

def default_sort_criteria(element_1, element_2): 
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def selection_sort(my_list, sort_crit):
    size = my_list["size"]
    elements = my_list["elements"]

    for i in range(size - 1):
        min_index = i
        # Se busca el menor desde i+1 hasta el final
        for j in range(i + 1, size):
            if sort_crit(elements[j], elements[min_index]):
                min_index = j
        # intercambiar si encontramos un nuevo mínimo
        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]

    return my_list

def insertion_sort(my_list, sort_crit):
    elements = my_list["elements"]
    size = my_list["size"]

    for i in range(1, size):
        j = i
        # desplazar elementos hacia la derecha si no cumplen el criterio
        while j > 0 and not sort_crit(elements[j - 1], elements[j]):
            exchange(my_list, j, j - 1)
            j -= 1
        

    return my_list

def shell_sort(my_list, sort_crit):
    
    elements = my_list["elements"]
    size = my_list["size"]

    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = elements[i]
            j = i
            while j >= gap and not sort_crit(elements[j - gap], temp):
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 2

    return my_list

    
def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def merge(l1, l2, sort_crit):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
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
    """
    Ordena una lista utilizando el algoritmo recursivo de ordenamiento Quick Sort.

    Se selecciona un elemento como pivote y se colocan los elementos menores a la izquierda y los mayores a la derecha de este elemento pivote.

    Si la lista es vacía o tiene un solo elemento, se retorna la lista original.
    """

    if size(my_list) <= 1:
        return my_list

    # Pivote: primer elemento
    pivot = first_element(my_list)

    less = new_list()
    equal = new_list()
    greater = new_list()

    # Recorrer Toda la lista nodo por nodo segun el pivote
    for i in range(size(my_list)):
        element = get_element(my_list, i)
        if sort_crit(element, pivot) and not sort_crit(pivot, element):
            add_last(less, element)
        elif sort_crit(pivot, element) and not sort_crit(element, pivot):
            add_last(greater, element)
        else:
            add_last(equal, element)

    # Recursión
    less_sorted = quick_sort(less, sort_crit) if size(less) > 1 else less
    greater_sorted = quick_sort(greater, sort_crit) if size(greater) > 1 else greater

    # Combinar resultado en la lista original
    my_list["elements"] = []
    my_list["size"] = 0

    for i in range(size(less_sorted)):
        add_last(my_list, get_element(less_sorted, i))

    for i in range(size(equal)):
        add_last(my_list, get_element(equal, i))

    for i in range(size(greater_sorted)):
        add_last(my_list, get_element(greater_sorted, i))

    return my_list
        
        