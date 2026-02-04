# # Input
# first_name = input("Enter first name\t") # Variable declaration
# last_name = input("Enter last name\t")

# # breakpoint()

# print(f"My name is {first_name} {last_name}") # Output

# first_name = input("Enter first name \n\n")

# paragraph = f"""
#     This is a paragraph 
#     stating {first_name}'s
#     biography
# """
# print(paragraph)


# .format() method


# paragraph = """
#     This is a paragraph 
#     stating {}'s {} {} {} {a} {b}
#     biography
# """.format(first_name, first_name, first_name, first_name, a=first_name, b= first_name)


# print(paragraph)

# WAP to
# Ask for input in terminal for user demography 
# and 
# format the string using f string as well as format method in str 
# and
# print the paragraph



# demographic_keys = ["full_name", "date_of_birth", "address", "gender", "contact", "religion"]

# identity = {i:input(f"Enter your {i} \t") for i in demographic_keys}

# # full_name
# # date_of_birth
# # address

# full_name = identity["full_name"]
# date_of_birth = identity["date_of_birth"]
# address = identity["address"]

# remaining_string = " \n".join(f"{k.upper()} : {v}" for k,v in identity.items() if k in demographic_keys[3:])

# # f-string
# f_paragraph = f"""
# Full Name : {full_name}
# Date Of Birth : {date_of_birth}
# Address : {address}
# {remaining_string}
# """# .format()

# format_paragraph = """
# Full Name : {}
# Date Of Birth : {a}
# Address : {b}
# {r}
# """.format(full_name, a=date_of_birth, b=address, r=remaining_string)

# print("-"*50)
# print(f"Using f-string \n {f_paragraph}\n")
# print("*"*50)
# print(f"Using .format() \n {format_paragraph}")
# print("-"*50)


# String Indexing And Slicing

# full_name = "Ram Hari Singh"
# #           # "0123456789"

# first_index_item = full_name[0] # Indexing
# first_five = full_name[0:5] # Slicing 

# print(f"First Index Item => {first_index_item}")
# print(f"Sliced Item => {first_five}")

# breakpoint()

full_name = str()


breakpoint()