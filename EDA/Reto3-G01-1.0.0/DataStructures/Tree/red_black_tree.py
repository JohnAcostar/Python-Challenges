from DataStructures.Tree import rbt_node as rn
from DataStructures.List import single_linked_list as sl

def new_map():
    """
    Crea una tabla de simbolos ordenada basa en un árbol rojo-negro (RBT) vacia
    """
    return {"root": None, "type": "RBT"}

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root["left"]) + size_tree(root["right"])


def rotate_left(h):
    """
    Rotación izquierda para compensar dos enlaces rojos consecutivos

    """
    x = h["right"]
    h["right"] = x["left"]
    x["left"] = h
    x["color"] = h["color"]
    h["color"] = 0  # RED
    x["size"] = h["size"]
    h["size"] = 1 + size_tree(h["left"]) + size_tree(h["right"])
    return x


def rotate_right(h):
    """
    Rotación a la derecha para compensar un hijo rojo a la derecha

    """
    x = h["left"]
    h["left"] = x["right"]
    x["right"] = h
    x["color"] = h["color"]
    h["color"] = 0  # RED
    x["size"] = h["size"]
    h["size"] = 1 + size_tree(h["left"]) + size_tree(h["right"])
    return x

def flip_node_color(node):
    """
    Cambia el color de un nodo

    """
    node["color"] = 1 if node["color"] == 0 else 0
    return node


def flip_colors(h):
    """
    ambia el color de un nodo y de sus dos hijos

    """
    flip_node_color(h)
    flip_node_color(h["left"])
    flip_node_color(h["right"])
    return h


def default_compare(key, element):
    if key == element["key"]:
        return 0
    elif key > element["key"]:
        return 1
    else:
        return -1

def is_red(node_rbt):
    """
    Indica si un nodo del arbol es rojo.
    """
    if node_rbt is None:
        return False  
    return node_rbt["color"] == 0  


def insert_node(h, key, value):
    if h is None:
        return rn.new_node(key, value)  

    cmp = default_compare(key, h)
    if cmp < 0:
        h["left"] = insert_node(h["left"], key, value)
    elif cmp > 0:
        h["right"] = insert_node(h["right"], key, value)
    else:
        h["value"] = value  

    # Balance fixes:
    if is_red(h["right"]) and not is_red(h["left"]):
        h = rotate_left(h)
    if is_red(h["left"]) and is_red(h["left"]["left"]):
        h = rotate_right(h)
    if is_red(h["left"]) and is_red(h["right"]):
        h = flip_colors(h)

    h["size"] = 1 + size_tree(h["left"]) + size_tree(h["right"])
    return h

def put(my_rbt, key, value):
    if my_rbt is None:
        my_rbt = new_map()

    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = 1  
    return my_rbt

def get_node(root, key):
    #Retorna el valor de la llave igual a key

    if root is None:
        return None

    if key == root["key"]:
        return root["value"]
    elif key < root["key"]:
        return get_node(root["left"], key)
    else:
        return get_node(root['right'], key)


def get(my_rbt, key):
    #Retorna el valor con llave igual a key
    
    if my_rbt is None or my_rbt['root'] is None:
        return None
    return get_node(my_rbt['root'], key)

def contains(my_rbt, key):
    #Informa si la llave key se encuentra en la tabla de hash.
    value = get(my_rbt, key)
    return value is not None
    
def size(my_rbt):
    """Retorna el número de entradas en la tabla de simbolos
    """
    if my_rbt is None:
        return 0
    return size_tree(my_rbt['root'])

def is_empty(my_rbt):
    """
    Informa si la tabla de simbolos se encuentra vacia.

    """
    return my_rbt is None or my_rbt['root'] is None

def key_set(my_rbt):
    """
    Retorna una lista con todas las llaves de la tabla.
    """
    keys = sl.new_list()
    if my_rbt is not None and my_rbt['root'] is not None:
        key_set_tree(my_rbt['root'], keys)
    return keys


def key_set_tree(root, key_list):
    """
    Recorre el árbol en inorder y añade las llaves a key_list.Construye una lista con las llaves de la tabla. Se recorre el arbol en inorder

    """
    if root is None:
        return key_list
    key_set_tree(root['left'], key_list)
    sl.add_last(key_list, root['key'])
    key_set_tree(root['right'], key_list)
    return key_list

def value_set(my_rbt):
    """
    Retorna una lista con los valores de la tabla.
    """
    values = sl.new_list()
    if my_rbt is not None and my_rbt['root'] is not None:
        value_set_tree(my_rbt['root'], values)
    return values


def value_set_tree(root, value_list):
    """
    Construye una lista con los valorers de la tabla. Se recorre el arbol en inorder
    """
    if root is None:
        return value_list
    value_set_tree(root['left'], value_list)
    sl.add_last(value_list, root['value'])
    value_set_tree(root['right'], value_list)
    return value_list

def get_min(my_rbt):
    """
    Retorna la llave mas a la izquierda de la tabla de simbolos
    """
    if my_rbt is None or my_rbt.get("root") is None:
        return None
    return left_key_node(my_rbt["root"])


def left_key_node(root):
    """
    Retorna la llave mas a la izquierda de la tabla de simbolos
    """
    if root is None:
        return None
    if root.get("left") is None:
        return root.get("key")
    return left_key_node(root["left"])


def get_max(my_rbt):
    """
    Retorna la llave mas a la derecha de la tabla de simbolos


    """
    if my_rbt is None or my_rbt.get("root") is None:
        return None
    return right_key_node(my_rbt["root"])


def right_key_node(root):
    """
    Retorna la llave mas a la derecha de la tabla de simbolos

    """
    if root is None:
        return 0
    if root.get("right") is None:
        return root.get("key")
    return right_key_node(root["right"])

def height(my_rbt):
    """
    Retorna la altura del arbol de busqueda
    """
    return height_tree(my_rbt.get("root"))


def height_tree(root):
    """
    Retorna la altura del arbol de busqueda

    """
    if root is None:
        return 0
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    return max(left_height, right_height) + 1 if root["left"] or root["right"] else 0



def keys(my_rbt, key_initial, key_final):
    """
    Retorna todas las llaves del arbol que se encuentren entre [key_initial, key_final].

    """
    key_list = sl.new_list()
    if my_rbt is not None and my_rbt['root'] is not None:
        keys_range(my_rbt['root'], key_initial, key_final, key_list)
    return key_list


def keys_range(root, key_initial, key_final, list_key):
    """
    Recorre el árbol en inorder y añade las llaves dentro del rango.
    """
    if root is None:
        return list_key
    if key_initial < root['key']:
        keys_range(root['left'], key_initial, key_final, list_key)
    if key_initial <= root['key'] <= key_final:
        sl.add_last(list_key, root['key'])
    if key_final > root['key']:
        keys_range(root['right'], key_initial, key_final, list_key)
    return list_key


def values(my_rbt, key_initial, key_final):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]
    """
    value_list = sl.new_list()
    if my_rbt is not None and my_rbt['root'] is not None:
        values_range(my_rbt['root'], key_initial, key_final, value_list)
    return value_list


def values_range(root, key_initial, key_final, list_values):
    """
    Retorna todas los valores del arbol que se encuentren entre [key_initial, key_final]

    """
    if root is None:
        return list_values
    if key_initial < root['key']:
        values_range(root['left'], key_initial, key_final, list_values)
    if key_initial <= root['key'] <= key_final:
        sl.add_last(list_values, root['value'])
    if key_final > root['key']:
        values_range(root['right'], key_initial, key_final, list_values)
    return list_values