def calculate_cart_total():
    total = 0
    for item in shopping_cart:
        total += menu[item[0]]
    return total

def payment():
    total = calculate_cart_total()
    while True:
        print("1. Pay in cash")
        print("2. Payment by card")
        choice = input("Select a payment method (1-2): ")
        if choice == '1':
            amount_paid = int(input('Enter the amount you will pay: '))
            if amount_paid >= total:
                change = amount_paid - total
                if change > 0:
                    print(f"Your change is: {change}")
                else:
                    print("Thank you for your payment!")
                break
            else:
                print("Insufficient cash payment. Please enter a sufficient amount.")
        elif choice == '2':
            payment_amount = int(input('Enter the payment amount: '))
            if payment_amount >= total:
                print("Payment successful!")
                break
            else:
                print("Insufficient funds on the card. Please enter a sufficient amount.")
        else:
            print("Incorrect entry. Please select 1 or 2.")

def payment ():
    while True:
        print("1. Pay in cash ")
        print("2. Payment by card")
        if choice == '1':
            ax = input('Enter how much you will pay ')
        elif choice == '2':
            xa = input('Enter the amount of opalty ')

def add_ingredients_to_the_pepperoni():
    x = input('if you want to add ingredients, write x')
    if x.lower() == 'x':
        sause = input('enter the name of the sauce you want to add')
        meat = input('enter the name of the ones you want meat that')
        vegetables = input('enter the name of the vegetables you want meat that')
        modified_item = ('have you added to the pepperoni', sause, meat, vegetables)
        menu['pepperoni'] = modified_item
        shopping_cart.append(modified_item)
    else:
        return

def add_ingredients_to_the_shawarma():
    sause = input('enter the name of the sauce you want to add')
    meat = input('enter the name of the ones you want meat that')
    vegetables = input('enter the name of the vegetables you want meat that')
    menu['shawarma'] = 'have you added to the shawarma', sause, meat, vegetables

def add_ingredients_to_the_burger():
    sause = input('enter the name of the sauce you want to add')
    meat = input('enter the name of the ones you want meat that')
    vegetables = input('enter the name of the vegetables you want meat that')
    menu['burger'] = 'have you added to the burger', sause, meat, vegetables

menuingredients = {
    'creamy garlic ketchup': 59,
    'tomato cucumber pepper parmesan cheese': 79,
    'cutlet bacon sausage': 100
}

menu = {
    'pepperoni': 999,
    'shawarma': 299,
    'burger': 159
}

print('welcome to our bar/cafe Late na mindalnem')
print(menu)
print(menuingredients)

shopping_cart = []

while True:
    print("1. pepperoni")
    print("2. shawarma")
    print("3. burger")
    print("4. Show shopping cart")
    print("5. Exit")
    print('6. payment ')
    choice = input("Select an action (1-6):")

    if choice == '1':
        add_ingredients_to_the_pepperoni()
    elif choice == '2':
        add_ingredients_to_the_shawarma()
    elif choice == '3':
        add_ingredients_to_the_burger()
    elif choice == '4':
        print("Shopping Cart:")
        for i in shopping_cart:
            print(i)
    elif choice == '5':
        break
    elif choice == '6':
        payment()
        print(calculate_cart_total())
        break
    else:
        print("Incorrect entry. Please select from 1 to 6.")

