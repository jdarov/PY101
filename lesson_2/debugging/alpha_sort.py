def alpha_insert(country_list, new_country):
    if new_country in country_list:
        return f"This country {new_country} is already in the list!"
    
    if country_list:
        for i, country in enumerate(country_list):
            if new_country < country:
                country_list.insert(i, new_country)
                return country_list
    
    country_list.append(new_country)
    return country_list
countries = ['Australia', 'Cuba', 'Senegal']

alpha_insert(countries, 'Brazil')
print(', '.join(countries))

print(', '.join(alpha_insert([], 'Brazil')))            # Inserting into an empty list

print(alpha_insert(['Brazil'], 'Australia'))  # At the beginning of a list

print(alpha_insert(['Brazil'], 'Cuba'))       # At the end of a list

print(alpha_insert(['Brazil'], 'Brazil'))   # Duplicate entry

name, grade = ('Josh', 'Passing?')
print(name)
print(grade)

def same(x):
    return x
print(6+4*same(4))