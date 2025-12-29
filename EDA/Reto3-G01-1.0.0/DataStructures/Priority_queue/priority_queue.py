from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import pq_entry as pqe


def default_compare_lower_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a menor."""
    return pqe.get_priority(father_node) <= pqe.get_priority(child_node)


def default_compare_higher_value(father_node, child_node):
    """Función de comparación por defecto para el heap orientado a mayor """
    return pqe.get_priority(father_node) >= pqe.get_priority(child_node)

def priority(my_heap, parent, child):
    """Indica si el parent tiene mayor prioridad que child."""
    return my_heap["cmp_function"](parent, child)

def size(my_heap):
    """Obtiene el número de elementos en el heap"""
    return my_heap["size"]


def is_empty(my_heap):
    """Verifica si la cola de prioridad está vacía."""
    return my_heap["size"] == 0


def swim(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la última posición del heap"""
    while pos > 1:
        parent = pos // 2
        parent_node = lt.get_element(my_heap["elements"], parent)
        child_node = lt.get_element(my_heap["elements"], pos)
        if not priority(my_heap, parent_node, child_node):
            lt.exchange(my_heap["elements"], parent, pos)
            pos = parent
        else:
            break

def insert(my_heap, priority_value, value):
    """Agrega una nueva entrada prioridad-valor al heap. Inserta la prioridad priority con valor value en el heap al final de la 
    lista de elementos y luego se hace swim para dejar el elemento en la posición correcta."""
    entry = pqe.new_pq_entry(priority_value, value)
    lt.add_last(my_heap["elements"], entry)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])
    return my_heap



def sink(my_heap, pos):
    """Deja en la posición correcta un elemento ubicado en la raíz del heap"""
    size = my_heap["size"]
    while 2 * pos <= size:
        j = 2 * pos
        left = lt.get_element(my_heap["elements"], j)
        if j < size:
            right = lt.get_element(my_heap["elements"], j + 1)
            if not priority(my_heap, left, right):
                j += 1
        if priority(my_heap, lt.get_element(my_heap["elements"], pos), lt.get_element(my_heap["elements"], j)):
            break
        lt.exchange(my_heap["elements"], pos, j)
        pos = j

def remove(my_heap):
    """Retorna el elemento del heap de mayor prioridad y lo elimina. Se reemplaza el primer elemento del heap 
    por el último elemento y se hace sink para dejar el elemento en la posición correcta."""
    if is_empty(my_heap):
        return None
    elements = my_heap["elements"]
    max_entry = lt.get_element(elements, 1)
    lt.exchange(elements, 1, my_heap["size"])
    lt.remove_last(elements)
    my_heap["size"] -= 1
    if my_heap["size"] > 0:
        sink(my_heap, 1)
    return pqe.get_value(max_entry)


def get_first_priority(my_heap):
    """Obtiene el elemento de mayor prioridad del heap sin eliminarlo"""
    if is_empty(my_heap):
        return None
    first_entry = lt.get_element(my_heap["elements"], 1)
    return pqe.get_value(first_entry)

def is_present_value(my_heap, value):
    """Busca si ya existe una entrada en el heap cuyo valor sea el value. Si existe se retorna
    la posición de la entrada que contiene el value. Si No existe se retorna el valor -1."""
    for i in range(1, my_heap["size"] + 1):
        entry = lt.get_element(my_heap["elements"], i)
        if pqe.get_value(entry) == value:
            return i
    return -1

def contains(my_heap, value):
    """Busca si ya existe una entrada en el heap cuyo valor sea el value. 
    Si existe se retorna True. En caso contrario, False."""
    return is_present_value(my_heap, value) != -1


def improve_priority(my_heap, priority_value, value):
    """
    Mejorar la prioridad de la pq_entry que tenga el value dado. 
    Funciona para MinPQ y MaxPQ.
    """
    pos = is_present_value(my_heap, value)
    if pos == -1:
        return my_heap

    entry = lt.get_element(my_heap["elements"], pos)
    pqe.set_priority(entry, priority_value)
    lt.change_info(my_heap["elements"], pos, entry)
    swim(my_heap, pos)
    sink(my_heap, pos)
    return my_heap

def new_heap(is_min_pq=True):
    """
    Crea un cola de prioridad indexada orientada a menor o mayor dependiendo del valor de is_min_pq

    """
    heap = {
        "elements": lt.new_list(),  
        "size": 0,
        "cmp_function": default_compare_lower_value if is_min_pq else default_compare_higher_value,
    }

    lt.add_last(heap["elements"], None)
    return heap