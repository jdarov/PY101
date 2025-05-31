from datetime import datetime

age = int(input('What is your age? '))
retire_age = int(input('At what age would you like to retire? '))

current_year = datetime.now().year

print(f"It's {current_year}. You will retire in {current_year+(retire_age-age)}")
print(f'You have only {retire_age-age} years of work to go!')