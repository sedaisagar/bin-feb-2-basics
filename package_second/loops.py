# Two kinds of loops
# for, while



full_name = "Shlok Pal"

for item in full_name:
    print(item)


count = 0
while (count < 5):
    print(f"I checked for {count}, got nothing!")
    count = count + 1

# WAP to
# Ask for input from terminal 
# for getting user name
# your implementation should exactly get single character on single scan
# concatenate those chars to make full user name


user_name = ""

length_of_name = int(input("Enter the length of your name : \n"))

for _ in range(length_of_name):
    user_name = user_name + input("Enter next character in your name : \n")


print(f"Finally your name is : => {user_name}")