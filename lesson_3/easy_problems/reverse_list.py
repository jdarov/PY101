numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reverse_list = numbers[len(numbers)-1::-1]

another_list = []
for idx in range(4, -1, -1):
    another_list.append(numbers[idx])

easy_list = list(reversed(numbers))
print(reverse_list)
print(another_list)
print(easy_list)
print(numbers)