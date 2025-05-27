def sum_nums(num1, num2):
    return num1 + num2 if all(isinstance(n, (int, float)) for n in (num1, num2)) else "Not a number"

print(sum_nums(1, 2))
print(sum_nums(1, '2'))