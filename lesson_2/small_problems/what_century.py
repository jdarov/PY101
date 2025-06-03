def century(year):
    # Calculate the century number
    century_number = (year - 1) // 100 + 1

    # Handle special case for 11th, 12th, 13th
    if 10 <= century_number % 100 <= 13:
        suffix = 'th'
    else:
        # Use last digit to determine the suffix
        last_digit = century_number % 10
        suffix = {
            1: 'st',
            2: 'nd',
            3: 'rd'
        }.get(last_digit, 'th')

    return f"{century_number}{suffix}"


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True