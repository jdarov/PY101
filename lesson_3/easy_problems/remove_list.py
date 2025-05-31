numbers = [1, 2, 3, 4]
new_numbers = numbers
numbers.clear()
print(numbers)
print(new_numbers)

numbers = [1, 2, 3, 4]
new_numbers = numbers
for dix in range(len(numbers)):
    numbers.pop(0)

print(numbers)
print(new_numbers)