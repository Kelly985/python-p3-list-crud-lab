def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(LIST, element):
    LIST.append(element)
    return LIST

def add_element_to_start_of_list(LIST, element):
    LIST.insert(0, element)
    return LIST

def remove_element_from_end_of_list(LIST):
    LIST.pop()
    return LIST

def remove_element_from_start_of_list(LIST):
    LIST.pop(0)
    return LIST

def retrieve_first_element_from_list(LIST):
    return LIST[0]

def retrieve_element_from_index(LIST, index):
    return LIST[index]

def retrieve_last_element_from_list(LIST):
    return LIST[-1]

my_list = create_a_list()

print(remove_element_from_start_of_list(my_list))

print(add_element_to_start_of_list(my_list, 10))

print(retrieve_last_element_from_list(my_list))

print(retrieve_element_from_index(my_list, 2))