def validate_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print('That is not a valid number.')

def total_bill(bill, percent):
    return bill * (1+(percent/100))

def tip(bill, percent):
    return bill * (percent/100)

def main():
    bill_amount = validate_input("What is the bill?\n$")
    tip_percentage = validate_input('What is the tip percentage?\n%')

    print(f'The tip is ${tip(bill_amount, tip_percentage):.2f}')
    print(f'The total is ${total_bill(bill_amount, tip_percentage):.2f}')

main()