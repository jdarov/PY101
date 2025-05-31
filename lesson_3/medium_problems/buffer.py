def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer   #now this is a shallow copy
    buffer2 = buffer + [new_element]   #this is a new list object with added element
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

#Function one will always mutate the old list and return the list called as an arg with changes
#function 2 reassings local variable buffer to the old list + new element
#   this means any changes mande in function 2 buffer will not change the old list

buffer_list = [1, 2, 3, 4, 5]
new_buffer = add_to_rolling_buffer1(buffer_list, 4, 6)
print(buffer_list)  #2, 3, 4, 5, 6
print(new_buffer)    #2, 3, 4, 5, 6

buffer_list = [1, 2, 3, 4, 5]
new_buffer = add_to_rolling_buffer2(buffer_list, 4, 6)
print(buffer_list) #1, 2, 3, 4, 5
print(new_buffer)  #2, 3, 4, 5, 6