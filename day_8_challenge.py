from random import randint


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.account_number} {self.balance}'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, float) or amount <= 0:
            print("Amount must be a positive float")
            return
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount


def create_customer(first_name, last_name):
    if not all(isinstance(x, str) for x in [first_name, last_name]):
        raise ValueError("First name and last name must be strings")
    return Customer(first_name, last_name, randint(1000000, 19999999), 0)


option_list = [
    "1. Create a new customer",
    "2. Deposit money",
    "3. Withdraw money",
    "4. View customer details",
    "5. Exit"
]


def display_options():
    for option in option_list:
        print(option)


def start():
    print('Welcome to the Bank Management System')
    first_name = input("please input your first name: ")
    last_name = input("please input your last name: ")
    customer = create_customer(first_name, last_name)

    while True:
        print('*' * 30)
        display_options()
        choice = input("Please select an option (1-5): ")
        if choice == '1':
            print("Customer created successfully.")
            print(customer)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)
            print(f"Deposited {amount}. New balance: {customer.balance}")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)
            print(f"Withdrew {amount}. New balance: {customer.balance}")
        elif choice == '4':
            print(customer)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


start()
