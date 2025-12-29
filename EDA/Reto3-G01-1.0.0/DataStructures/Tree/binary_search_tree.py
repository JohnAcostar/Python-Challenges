from DataStructures.Tree import bst_node as bn
from DataStructures.List import single_linked_list as sl



def new_map():
    """
    Crea una nueva tabla de simbolos
    (map) ordenada basada en un árbol binario de búsqueda (BST).
    """
    return {"root": None}


def put(my_bst, key, value):
    """
    Agrega un nuevo nodo llave-valor a un árbol binario de búsqueda (BST).
    Si la llave ya existe, se actualiza el value del nodo.
    """
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


def insert_node(root, key, value):
    """
    Inserta un nuevo nodo llave-valor en el árbol binario de búsqueda
    (BST) de manera recursiva.


    """
    if root is None:
        return bn.new_node(key, value)

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        # Si la llave ya existe, actualizamos el valor
        root["value"] = value

    # Actualizamos el tamaño del nodo
    left_size = root["left"]["size"] if root["left"] else 0
    right_size = root["right"]["size"] if root["right"] else 0
    root["size"] = 1 + left_size + right_size

    return root


def get(my_bst, key):
    """
    Busca un nodo en el árbol binario de búsqueda (BST) y devuelve su valor.

    """
    return get_node(my_bst["root"], key)


def get_node(root, key):
    """Busca un nodo en el árbol binario de búsqueda (BST) de manera recursiva."""
    if root is None:
        return None

    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:
        return bn.get_value(root)

def size(my_bst):
    """
    Retorna el número de entradas en la tabla de simbolos

    """
    root = my_bst["root"]
    return size_tree(root)


def size_tree(root):
    """
    Retornar el número de entradas en la a partir del nodo root
    """
    if root is None:
        return 0
    else:
        left_size = size_tree(root["left"])
        right_size = size_tree(root["right"])
        return 1 + left_size + right_size

def contains(bst, key):
    """Informa si la llave key se encuentra en la tabla de hash."""
    return get(bst, key) != None

def is_empty(bst):
    #Informa si la tabla de simbolos se encuentra vacia.

    return size(bst) == 0

def key_set_tree(root, key_list):
    #Retorna una lista con todas las llaves de la tabla.

    if root is None:
        return
    key_set_tree(root["left"], key_list)
    sl.add_last(key_list, root["key"])
    key_set_tree(root["right"], key_list)

def key_set(my_bst):
    #Retorna una lista con todas las llaves de la tabla.

    key_list = sl.new_list()
    key_set_tree(my_bst.get("root"), key_list)
    return key_list


def value_set_tree(root, value_list):
    #Retorna una lista con los valores de la tabla.
    if root is None:
        return
    value_set_tree(root["left"], value_list)
    sl.add_last(value_list, root["value"])
    value_set_tree(root["right"], value_list)

def value_set(my_bst):
    #Retorna una lista con los valores de la tabla.
    value_list = sl.new_list()
    value_set_tree(my_bst.get("root"), value_list)
    return value_list


def get_min_node(root):
    #Retorna la llave mas pequeña de la tabla de simbolos


    if root is None:
        return None
    while root["left"] is not None:
        root = root["left"]
    return root

def get_min(my_bst):
    #Retorna la llave mas pequeña de la tabla de simbolos

    min_node = get_min_node(my_bst.get("root"))
    if min_node is None:
        return None
    return min_node["key"]


def get_max_node(root):
    #Retorna la llave mas grande de la tabla de simbolos

    if root is None:
        return None
    while root["right"] is not None:
        root = root["right"]
    return root

def get_max(my_bst):
    #Retorna la llave mas grande de la tabla de simbolos
    max_node = get_max_node(my_bst.get("root"))
    if max_node is None:
        return None
    return max_node["key"]

def _node_size(node):
    if node is None:
        return 0
    return node.get("size", 0)

def delete_min_tree(root):
    #Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root

def delete_min(my_bst):
    #Encuentra y remueve la llave mas pequeña de la tabla de simbolos y su valor asociado.
    my_bst["root"] = delete_min_tree(my_bst.get("root"))
    return my_bst


def delete_max_tree(root):
    #Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_tree(root["right"])
    root["size"] = 1 + _node_size(root["left"]) + _node_size(root["right"])
    return root

def delete_max(my_bst):
    #Encuentra y remueve la llave mas grande de la tabla de simbolos y su valor asociado.
    my_bst["root"] = delete_max_tree(my_bst.get("root"))
    return my_bst

def height_tree(root):
    #Retorna la altura del arbol de busqueda
    if root is None:
        return 0
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    return max(left_height, right_height) + 1 if root["left"] or root["right"] else 0

def height(my_bst):
    #Retorna la altura del arbol de busqueda
    return height_tree(my_bst.get("root"))

def keys_range(root, key_initial, key_final, list_key):
    """
    Retorna todas las llaves del árbol que se encuentren entre [key_initial, key_final].
    Es usada por keys().
    """
    if root is None:
        return

    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)

    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_key, root["key"])

    if key_final > root["key"]:
        keys_range(root["right"], key_initial, key_final, list_key)


def keys(my_bst, key_initial, key_final):
    """
    Retorna todas las llaves del árbol que se encuentren entre [key_initial, key_final].
    """
    list_key = sl.new_list()  
    root = my_bst.get("root")

    keys_range(root, key_initial, key_final, list_key)

    return list_key


def values_range(root, key_initial, key_final, list_value):
    #Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    if root is None:
        return
    if key_initial < root["key"]:
        values_range(root["left"], key_initial, key_final, list_value)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_value, root["value"])
    if key_final > root["key"]:
        values_range(root["right"], key_initial, key_final, list_value)

def values(my_bst, key_initial, key_final):
    #Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    list_value = sl.new_list()
    values_range(my_bst.get("root"), key_initial, key_final, list_value)
    return list_value

def default_compare(key, element):
    """
    Función de comparación por defecto. Compara una llave con la llave de un elemento llave-valor.
    """
    if key == bn.get_key(element):
        return 0
    elif key > bn.get_key(element):
        return 1
    return -1