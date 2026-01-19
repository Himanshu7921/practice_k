import random

class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.account_number = None
        self.account_balance = 0
    
    def get_details(self):
        print()
        print(f"Person Name: {self.name} | Person Age: {self.age}")
        print(f"Account Number: {self.account_number} | Bank Balance: {self.account_balance}")
        print()

class BankAccount:
    def __init__(self, person):
        self.person = person
        self.person.account_number = random.randint(10000, 999999)

    @staticmethod
    def send_money(person_1, person_2, how_much_to_send):
        person_1.account_balance = person_1.account_balance - how_much_to_send
        person_2.account_balance = person_2.account_balance + how_much_to_send

p1 = Person(name = "Roshan", age = 19)
p2 = Person(name = "Rohit", age = 21)

print("Before Creating Account\n")
p1.get_details()
p2.get_details()


account_1 = BankAccount(p1)
account_2 = BankAccount(p2)

print("After Creating Account\n")
p1.get_details()
p2.get_details()

BankAccount.send_money(person_1 = p1, person_2 = p2, how_much_to_send = 100)

print("After Creating Account\n")
p1.get_details()
p2.get_details()