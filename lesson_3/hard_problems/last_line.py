dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)  #[1, 2]
print(dictionary) #{'first' : [1, 2]}

#the list in dict is mutable so it points to second object
#any changes WILL affect dictionary in the list 