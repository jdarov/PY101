def greetings(full_name_list, title_occ_dict):
    full_name = ' '.join(full_name_list)
    title = title_occ_dict.get('title', 'Launch School').title()
    occupation = title_occ_dict.get('occupation', 'Student').title()

    return f'Hello, {full_name}! Nice to have a {title} {occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

greeting = greetings(
    ['Some', 'Other', 'Name'],
    {}
)

print(greeting)
#Hello, Some Other Name! Nice to have a Launch School Student around.