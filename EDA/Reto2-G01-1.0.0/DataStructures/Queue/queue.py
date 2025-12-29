def new_queue():
    retorno = {"first": None, 
               "last": None, 
               "size": 0,
    }
    
    return retorno

def enqueue(my_queue, element):
    
    
    new_node = {"info": element, "next": None}
    if my_queue["first"] is None:  # lista vacía
        my_queue["first"] = new_node
        my_queue["last"] = new_node
    else:
        my_queue["last"]["next"] = new_node
        my_queue["last"] = new_node
    my_queue["size"] += 1
    return my_queue

def dequeue(my_queue):
    
    if my_queue["size"] == 0:
        raise Exception("IndexError: list index out of range")

    value = my_queue["first"]["info"]

    my_queue["first"] = my_queue["first"]["next"]

    if my_queue["first"] is None:
        my_queue["last"] = None

    my_queue["size"] -= 1

    return value

def peek(my_queue):
    
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    return my_queue["first"]["info"]

def is_empty(my_queue):
    
    return my_queue["size"] == 0

def size(my_queue):
    
    retorno = my_queue["size"]
    return retorno