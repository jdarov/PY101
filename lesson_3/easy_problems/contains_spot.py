ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print("Spot" in ages.keys())

additional_ages = {'Marilyn': 22, 'Spot': 237}
for key, value in additional_ages.items():
    ages[key] = value

print(ages)