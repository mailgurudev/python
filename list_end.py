def list_ends(a_list):
    return  [a_list[0], a_list[len(a_list)-1]]

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list_ends(a))