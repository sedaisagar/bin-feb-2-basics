# class PersonUtilities:
#     def get_name(self):
#         self.name = input("Enter your name \n")
    
#     def get_age(self):
#         self.age = input("Enter your age \n")    

#     def get_address(self):
#         self.address = input("Enter your address \n")

#     def represent(self):
#         print(f"NAME :: {self.name}, AGE :: {self.age}, ADDRESS :: {self.address}")

# class Person(PersonUtilities): # Pascal Case ## Inheritance
#     # # Attributes
    
#     # Constructor
#     def __init__(luv):
#         luv.get_name()
#         luv.get_age()
#         luv.get_address()
#         # luv.name = name
#         # luv.age = age
#         # luv.address = address

#     def get_name(self):
#         self.name = input("Enter your name \n")
    
#     def get_age(self):
#         self.age = input("Enter your age \n")    

#     def get_address(self):
#         self.address = input("Enter your address \n")

#     def represent(self):
#         # print(f"NAME :: {self.name}, AGE :: {self.age}, ADDRESS :: {self.address}")
#         super().represent() # Parent class function trigger / call 


# instance = Person() #Instantiation / Object creation 

# instance.represent() 



# Multiple Inheritance


# class A:
#     def h1(self):
#         print("I'm H1")


# class B:
#     def h2(self):
#         print("I'm H2")


# class C(A,B): # A, B are inherited in C, So this is multiple inheritance
#     def h3(self):
#         print("I'm H3")



# instance = C()

# instance.h1()
# instance.h2()
# instance.h3()


# MultiLevel Inheritance

# class A:
#     def h1(self):
#         print("I'm H1 from A")

#     def h2(self):
#             print("I'm H2 from A")


# class B:
#     def h1(self):
#         print("I'm H1 from B")
#         # super().h1()

#     def h2(self):
#         print("I'm H2 from B")
#         # super().h2()


# class C(A,B): # A, B , C are in multilevel inheritance

#     def h3(self):
#         print("I'm H3")


# instance = C()

# instance.h1()
# instance.h2()
# instance.h3()

# breakpoint()

# C.mro()

# Scan Person
# Print Person
# Last Child, Inheriting class, print something like "all worked successfully" 


# class Scanner:
#     list_of_persons = []
#     def scan_person(self):
#         for _ in range(5):
#             self.list_of_persons.append(
#                 {
#                     "name":input("Enter name : \t"),
#                     "age":input("Enter age : \t"),
#                     "address": input("Enter address : \t")
#                 }
#             )

# class Calculator(Scanner):
#     def __init__(self):
#         self.scan_person()

#     def analyze_mean_age(self):
#         self.mean_age = sum(
#             [int(i["age"]) for i in self.list_of_persons]
#         ) / len(self.list_of_persons) 

# class Printer(Calculator):
#     def __init__(self):
#         super().__init__()
#         self.analyze_mean_age()

#     def print_person(self):
#         def maker(i):
#             return f"""
#                 Name: {i["name"]}
#                 AGE : {i["age"]}
#                 ADDRESS : {i["address"]}
#                 ------------------------------
#             """
#         all_dems = " \n".join(
#             maker(i) for i in self.list_of_persons
#         )


#         mean_age = f"""
#         Mean AGE : {self.mean_age}
#         """

#         print(all_dems, "\n", mean_age)

# class Child(Printer):
#     def __init__(self):
#         super().__init__()
#         self.print_person()


# instance = Child()




class BankAccount:
    account_number, balance = 123456789, 50000
    interest_earned = 0

    def deposit(self, amount):
            self.balance = self.balance + amount
            return f"""
                TOTAL BALANCE {self.balance} \n DEPOSIT AMT {amount}
            """

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return f"""
                REMAINING BALANCE {self.balance} \n WITHDRAWL AMT {amount}
            """

    def get_balance(self):
        return f"YOUR CURRENT BALANCE IS :: {self.balance}"


class SavingsAccount(BankAccount):
    ir = 5
    def add_interest(self):
        earned_interest = (self.balance * (5 /100))
        self.balance += earned_interest
        self.interest_earned += earned_interest

        return f"""
            INTEREST CALCULATED :: {earned_interest} \n
            TOTAL INTEREST EARNED TILL NOW :: {self.interest_earned} \n
            TOTAL BALANCE :: {self.balance}
        """

instance = SavingsAccount()
while True:

    welcome_msg = f"""
    Welcome to the world bank. \n
    What do you want to do with your bank account!
    Choices: \n
    d :: DEPOSIT
    w :: WITHDRAW
    g :: GET BALANCE
    i :: ADD INTEREST
    \n 
    """
    print(welcome_msg)

    mode = input("Enter the mode \t")
    output = ""
    match mode:
        case "d":
            deposit_amt = float(input("Enter the amount to withdraw \t"))
            output = instance.deposit(deposit_amt)
        case "w":
            withdrwal_amt = float(input("Enter the amount to withdraw \t"))
            output = instance.withdraw(withdrwal_amt)
        case "g":
            output = instance.get_balance()
        case "i":
            output = instance.add_interest()
        case _:
            print(f"You provided illegal option {mode}")
            break
    
    print(output, "\n")