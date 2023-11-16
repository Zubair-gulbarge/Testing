# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} says Woof!")

# # Creating an object of the Dog class
# my_dog = Dog("Buddy", 3)

# # Accessing attributes and calling a method
# print(f"{my_dog.name} is {my_dog.age} years old.")
# my_dog.bark()

# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# # Creating objects of the derived classes
# my_cat = Cat("Feline")
# my_dog = Dog("Canine")

# # Calling the overridden method
# my_cat.make_sound()
# my_dog.make_sound()

# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance  # Protected attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposit successful. New balance: {self._balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrawal successful. New balance: {self._balance}")
#         else:
#             print("Invalid withdrawal amount.")

# # Creating an object of the BankAccount class
# account = BankAccount(1000)

# # Performing transactions
# account.deposit(500)
# account.withdraw(200)
