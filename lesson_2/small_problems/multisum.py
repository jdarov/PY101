def multisum(n):
    sum = 0
    for i in range(1, n +1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)