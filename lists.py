def remove_elements(list_to_remove_elements):

    if len(list_to_remove_elements) > 5:
        list_to_remove_elements.pop(5)
    if len(list_to_remove_elements) > 4:
        list_to_remove_elements.pop(4)
    if len(list_to_remove_elements) > 0:
        list_to_remove_elements.pop(0)
    return list_to_remove_elements

list_to_remove_elements = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list_to_remove_elements))


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

list_to_add_elements = ['Red', 'Green', 'White', 'Black']
print(add_elements(list_to_add_elements))

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False
    
list_to_check = []
print(is_empty(list_to_check))



def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        if list_to_compare1[2] != list_to_compare2[2]:
            return False
    if len(list_to_compare1) < 3 and len(list_to_compare2) < 3:
        return False
    if len(list_to_compare1) < 3 and len(list_to_compare2) >= 3:
        return False
    if len(list_to_compare1) >= 3 and len(list_to_compare2) < 3:
        return False

    
list_to_compare1 = ['Black', 'Pink', 'Green', 'White']
list_to_compare2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
print(check_lists(list_to_compare1, list_to_compare2))




def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify[0])  >= 2:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:2] 

    elif len(list_of_lists_to_modify[0])  == 1:
        list_of_lists_to_modify[0] = list_of_lists_to_modify[0][:1]

    else:
        list_of_lists_to_modify[0] = []
       
        
    
    if len(list_of_lists_to_modify[1])  >= 4:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:4]
        
    elif len(list_of_lists_to_modify[1])  >= 3:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:3]
        
    elif len(list_of_lists_to_modify[1])  >= 2:
        list_of_lists_to_modify[1] = list_of_lists_to_modify[1][1:2]
        
    else: 
        list_of_lists_to_modify[1] = []

    
    if len(list_of_lists_to_modify[2]) >= 2:
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-2:] 

    elif len(list_of_lists_to_modify[2])  == 1:
        list_of_lists_to_modify[2] = list_of_lists_to_modify[2][-1:]

    else:
        list_of_lists_to_modify[2] = []
       
    return list_of_lists_to_modify

list_of_lists_to_modify = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]] 
print(list_of_lists(list_of_lists_to_modify))
