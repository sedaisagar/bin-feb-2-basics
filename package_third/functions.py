# Functions in python


#  Input , OutPut

# -> number of inputs 
# -> number of outputs

# Input Output
#   X     ✔
#   ✔     X
#   X     X
#   ✔     ✔


# Function definition


# def add_two_numbers():
#     a,b=1,2
#     sum_of_two_numbers = a+b
#     print(sum_of_two_numbers)
#     # return sum_of_two_numbers
#     # return 

# sum_of_two_numbers = add_two_numbers()
# sum_of_two_numbers = sum([1,2,3,4,5,6,7,8,9,0,])

# print(f"Sum of two numbers is {sum_of_two_numbers}")

#  WAP
# Ask for first_name, middle_name, last_name from terminal
# Write a user defined function
# that accepts first_name, middle_name, last_name 
# concatenate those names to make full_name
# return the full_name and print the full_name

# String Concatenation

# "" + ""

# first_name, middle_name, last_name = "      Pinki", "Kumari", "Singh     "
# full_name = f"{first_name} {middle_name} {last_name}"

# print(f"My name {full_name.strip()} is the ultimate!")



# def concatenate_names(first_name, middle_name=None, last_name=None, *args):
#     for i in args:
#         print(i)


# concatenate_names("Md", "Shekh", middle_name="Al", first_name="Bin", last_name="Salman")



# names = [input("Enter the names \n") for _ in range(5)]

# def concat_names(*args):
#     return " ".join(args)

# names = ["Anubhav", "Bin", "Shekh", "Al", "Rasid"]

# # *names => "Anubhav", "Bin", "Shekh", "Al", "Rasid"
# print(concat_names(*names))


# Keyword arguments


# def concatenate_names(first_name, middle_name=None, last_name=None, **kwargs):
#     print(first_name, middle_name, last_name, kwargs)

# names = ["Anubhav", "Bin", "Shekh", "Al", "Rasid"]

# name_dict = {f"name_{i}":names[i] for i in range(5)}

# # {'name_0': 'Anubhav', 'name_1': 'Bin', 'name_2': 'Shekh', 'name_3': 'Al', 'name_4': 'Rasid'}
# # =>
# # name_0='Anubhav',name_1='Bin',...
# concatenate_names(first_name=names[0], middle_name=names[1], last_name=names[2], **name_dict)

import time
from datetime import datetime

def beautify(func):
    def adder(*args, **kwargs):
        
        print(f"Starting the execution at {datetime.now()}")
        arg_values = [i if isinstance(i, int) else ( int(i) if str(i).isnumeric() else 0 ) 
                        for i in args]

        key_values = [i if isinstance(i, int) else ( int(i) if str(i).isnumeric() else 0 ) 
                        for i in kwargs.values()]
        
        total_items = [*arg_values, *key_values] # Combining / Merging two lists
    
        for i in range(5):
            print(f"Sleeping for #{i}")
            time.sleep(1)
            print(f"Waking for #{i}")

        respo = func(total_sum=sum(total_items))

        print(f"Finished the execution at {datetime.now()}")
        
        return respo
    
    return adder

@beautify
def print_full_name(*args, **kwargs):
    print(f"The total sum of provided args and kwargs values is {kwargs["total_sum"]}")

print_full_name("12", 10,20,40,50, value=8, value2=1250)