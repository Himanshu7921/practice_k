import random

class Person:
    def __init__(self, name, age, bank_name):
        self.age = age
        self.name = name
        self.account_number = None
        self.account_balance = 0
        self.bank_name = bank_name
    
    def get_details(self):
        print()
        print(f"Person Name: {self.name} | Person Age: {self.age}")
        print(f"Bank Name: {self.bank_name} | Account Number: {self.account_number} | Bank Balance: {self.account_balance}")
        print()

class BankAccount:
    def __init__(self, person):
        self.person = person
        self.person.account_number = random.randint(10000, 999999)

    @staticmethod
    def send_money(person_1, person_2, how_much_to_send):
        if person_1.account_balance > how_much_to_send:
            person_1.account_balance = person_1.account_balance - how_much_to_send
            person_2.account_balance = person_2.account_balance + how_much_to_send
        else:
            print("Payment failed due to insufficient balance")

p1 = Person(name = "Roshan", age = 19, bank_name = "HDFC")
p1.account_balance = 100
p2 = Person(name = "Rohit", age = 21, bank_name = "SBI")
p2.account_balance = 130

account_1 = BankAccount(p1)
account_2 = BankAccount(p2)

print("Before Sending Money...\n")
p1.get_details()
p2.get_details()

print("After Sending Money...\n")

BankAccount.send_money(person_1 = p1, person_2 = p2, how_much_to_send = 30)
p1.get_details()
p2.get_details()

"""
Things to Change:

1. Keep the logic for sending money from one person to another (using account numbers) clearly separated and organized.

2. Add a feature where a person can choose which bank they want to open an account in.
    Tip: Create different classes for each bank (like SBI and HDFC) and make them inherit from a common Bank class.

3. Make sure a person is allowed to have accounts in multiple banks.
"""