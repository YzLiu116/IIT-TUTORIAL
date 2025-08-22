print('Welcome to the Python Coffee Shop!')

customer_name = input('What is your name? ')
print('Hello, ' + customer_name + '! Let\'s order some coffee.')

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50  # new drink

while True:
    # Show menu
    print('\nMenu:')
    print('Coffee: $' + str(price_coffee))
    print('Latte: $' + str(price_latte))
    print('Mocha: $' + str(price_mocha))

    # Get order
    choice = input('What would you like to order? (coffee/latte/mocha): ').lower()

    if choice == 'coffee':
        cost = price_coffee
    elif choice == 'latte':
        cost = price_latte
    elif choice == 'mocha':
        cost = price_mocha
    else:
        print('Sorry, we do not have that.')
        cost = 0

    if cost > 0:
        quantity = int(input('How many cups would you like? '))
        total_cost = cost * quantity

        # Quantity discount
        if quantity > 1:
            print('You get a discount of $1.00!')
            total_cost -= 1.00

        # Student discount
        is_student = input('Are you a student? (yes/no): ').lower()
        if is_student == 'yes':
            print('Student discount applied (10% off).')
            total_cost *= 0.9

        print('Your total is: $' + str(round(total_cost, 2)))
        print('Thank you, ' + customer_name + '!')

    # Ask if they want to order again
    another = input('\nWould you like to order another drink? (yes/no): ').lower()
    if another == 'no':
        print('Goodbye, ' + customer_name + '! Please come again.')
        break

