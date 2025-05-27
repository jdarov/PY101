SQFT_PER_SQM = 10.7639

def ask_for_dimension(prompt):
    while True:
        dimension = input(prompt)
        try:
            float_dimension = float(dimension)
            if float_dimension <= 0:
                print('You must enter a positive value. Try again')
                continue
            return float_dimension
        except ValueError:
            print('Sorry, that is not a valid resonse')

def feet_or_meters():
    while True:
        user_input = input('Please enter "f" for feet or "m" for meters: ')
        if user_input.lower() == 'f' or user_input.lower() == 'm':
            return user_input.lower()
        print('That was not a valid choice. Please try again')

def area_of_room(l, w):
    return l * w

def main():
    print('Welcome to area of room calculator!')
    measurement = feet_or_meters()
    length_of_room = ask_for_dimension('Please enter the length of the room: ')
    width_of_room = ask_for_dimension('Please enter the width of the room: ')
    area = area_of_room(length_of_room, width_of_room)

    if measurement == 'f':
        print(f'The area of the room is {area/SQFT_PER_SQM:.2f} sq. meters')
        print(f'and {area:.2f} sq. ft')
    else:
        print(f'The area of the room is {area:.2f} sq. meters ')
        print(f'and {area * SQFT_PER_SQM:.2f} sq. ft')
main()