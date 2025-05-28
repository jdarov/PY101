"""
Ask user for the amount of a loan, the APR and the duration of the loan in years
Validate input is correct and return a monthly payment amount based on input
"""
def validate_input(prompt):
    """
    Function to validate user input is a number, not an invalid input like str
    param: prompt, the prompt user will respond to
    """
    while True:
        try:
            user_input = float(input(prompt).replace(',', ''))
            if user_input < 0:
                print('This should be a postive number. Try again\n')
                continue
            return user_input
        except ValueError:
            print('That is not a proper number. Please type a number.\n')

def monthly_interest_rate(apr):
    """
    Converts the APR (annual percent) given by user into a monthly rate
    If user enters a number < 1, asks for validation if entered correctly
    """
    if apr < 1:
        while True:
            try:
                response = input(f"It looks like you entered {apr:.2f}. Did you mean:\n"
                                 f"  1) {apr * 100:.2f}% (percent APR)\n"
                                 f"  2) {apr:.2f}% (decimal APR)\n"
                                 "Enter the correct value: ")
                user_input = float(response)
                if user_input == apr:
                    break
                if user_input == apr * 100:
                    apr = user_input
                    break
                print(f"\n==>Please enter either {apr:.2f} or {apr*100:.2f}\n")
            except ValueError:
                print("Invalid number. Please enter a number\n")
    return (apr/12)/100

def monthly_duration(years):
    """
    Converts the amount of years of loan given by user into monthly duration
    """
    return years * 12

def total_monthly_payment(loan_amt, monthly_int, loan_dur):
    """
    Function to return the total monthly payment using the algorithm for determining this from
    param: loan_amt: total cost of loan
    monthly_int: interest on loan, converted to a monthly basis
    loan_dur: total time of the loan, in months
    """
    if monthly_int == 0:
        return loan_amt / loan_dur
    return loan_amt * (monthly_int / (1 - (1 + monthly_int) ** (-loan_dur)))

def get_user_inputs():
    """
    Return the user input in the form of total loan amount, monthly interest rate
    and duration in months
    """
    total = validate_input('What is the total loan amount? ')
    month_interest = monthly_interest_rate(validate_input('What is the APR of the loan? '))
    month_duration = monthly_duration(validate_input('What is the duration of loan, in years? '))

    return total, month_interest, month_duration

def main():
    """
    Main program body
    """
    print("Welcome to the LOAN CALCULATOR!")
    user_continue = ''
    while user_continue.strip().lower() not in {'no', 'n', 'stop'}:
        loan_amount, monthly_interest, loan_duration = get_user_inputs()
        total_monthly_cost = total_monthly_payment(loan_amount, monthly_interest, loan_duration)

        print(f'\nBased off the total loan amount of ${loan_amount:,}')
        print(f'And a monthly interest rate of %{monthly_interest*100:.2f}')
        print(f'And a loan duration of {int(loan_duration)} months')

        print(f'Your total monthly cost will be ${total_monthly_cost:,.2f}\n')

        user_continue = input('Would you like to do another calculation? ')

main()
