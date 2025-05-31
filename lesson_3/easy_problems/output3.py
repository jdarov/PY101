my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()    #this creates a SECOND object with a copy of the list, not pointing to same object
my_list2[0]['first'] = 42
print(my_list1)   #[{"first": "value1"}, {"second": "value2"}, 3, 4, 5]