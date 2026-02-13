# file = open("./sample.txt", "a")

# file.write("This is sample text\n"*50)

# file.close()
# # breakpoint()


# with open("./sample.txt", "a") as file:
#     file.write("This is sample text\n"*50)

with open("./sample.txt", "r") as file:
    # file.write("This is sample text\n"*50)
    # content = file.read()
    content = file.readlines()
    for i in content:
        print(i)

name, age, address = "","",""

f"Name : {name}, Age: {age}, Address : {address}"



