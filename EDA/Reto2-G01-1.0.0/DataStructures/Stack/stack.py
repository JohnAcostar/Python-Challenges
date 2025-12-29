def new_stack():
    stack = {"first": None, 
               "last": None, 
               "size": 0,
    }
    return stack

def is_empty(my_stack):    
    if my_stack["size"] == 0:
        return True
    else:
        return False


def push(my_stack, element):
    # Añadir un elemento al tope del stack
    new_node = {"info": element, "next": my_stack["first"]}
    my_stack["first"] = new_node
    if my_stack["last"] is None:
        my_stack["last"] = new_node
    my_stack["size"] += 1
    return my_stack

def pop(my_stack):
    if is_empty(my_stack) == True:
        raise Exception("EmptyStructureError: stack is empty")

    value = my_stack["first"]["info"]

    my_stack["first"] = my_stack["first"]["next"]

    if my_stack["first"] is None:
        my_stack["last"] = None

    my_stack["size"] -= 1
    
    return value

def top(my_stack):
    if is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    
    return my_stack["first"]["info"]

def size(my_stack):

    return my_stack["size"]