# Immutable
salaries = (100000,200000) #or tuple(1,2)

# Accessing Tuple Items
# print(salaries[0])
# print(salaries[1])


# Trying to mutate 

# salaries[1] = 1456423

for item in salaries:
    print(item)

# Tuple Unpacking

a,b = salaries

print(a,b)


# Type Casting

salaries_list = list(salaries) # Tuple -> List 

print(salaries_list)

salaries_tuple = tuple(salaries_list) # List -> Tuple

print(salaries_tuple)

# List of Tuples
[
    ("name", "address", "religion", "age")
]

# List of Dictionaries
[
    dict(name="", address="", religion="", age=""),
    {"name":"","address":"", "religion":"", "age":""},
]


list_of_tups = []
list_of_dicts = []

for _ in range(2):
    name = input("Enter the name \t")
    address = input("Enter the address \t")
    religion = input("Enter the religion \t")
    age = input("Enter the age \t")
    print("*"*50)

    list_of_tups.append((name, address, religion, age))

    dem = dict()
    dem.update(name=name)
    dem.setdefault("address", address)
    dem["religion"] = religion
    dem["age"] = age
    list_of_dicts.append(dem)

print("*"*50)
print(list_of_tups)
print("*"*50)
print(list_of_dicts)
print("*"*50)