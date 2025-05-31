def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:  #If a remainder of a number/number is 0, then it divides into it evenly, meaning its a factor of that number
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(8))
print(factors(-1))