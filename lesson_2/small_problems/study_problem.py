lst = [1, 2, 3]

def empty_list(lst):
    for idx in range(len(lst)):
        del lst[0]
    return lst

print(empty_list(lst))
print(lst)