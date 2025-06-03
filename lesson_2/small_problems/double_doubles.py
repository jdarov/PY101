def is_double(number):
    string_number = str(number)
    if len(string_number) % 2 == 0:
        if (string_number[:len(string_number)//2] == string_number[len(string_number)//2:]):
            return True
    return False

def twice(number):
    if is_double(number):
        return number
    return number * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True