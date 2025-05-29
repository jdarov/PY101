import json

practice_dict = {
    'names' : {
        'first name': ['Josh', 'Mutti', 'Rita'],
        'last name': ['Darovitz', 'Sutton', 'Iurtaeva'],
    },
    'relationship' : ['myself', 'grandmother', 'wife'],
}
print(practice_dict.get('names'))

print(practice_dict['names']['first name'])

first_names = practice_dict['names']['first name']
last_names = practice_dict['names']['last name']
relationships = practice_dict['relationship']

contact_list = []
for first, last, relationship in zip(first_names, last_names, relationships):
    people = {
        'first_name': first,
        'last_name': last,
        'relationship': relationship
    }
    contact_list.append(people)
with open('people.json', 'w', encoding='utf-8') as file:
    json.dump(contact_list, file, indent=4)

with open('people.json', 'r') as file:
    new_list = json.load(file)

finished_list = []
for dicts in new_list:
    finished_list.append(dicts['first_name'] + ' ' + dicts['last_name'])

print(', '.join(finished_list))