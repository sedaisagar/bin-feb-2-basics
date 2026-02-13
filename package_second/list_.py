# students = ["Ram","Shyam"] # or list() # String data list

# roll_numbers = [1,2] # Int data list

# fees = [5000.5, 6000.7] # Float data list

# is_passsed = [False, True]

# for index, value in enumerate(students):
#     dem = f"""
#     Student Name  :{value}
#     Roll Number : {roll_numbers[index]}
#     Fee : {fees[index]}
#     Has Passed : {'Pass' if is_passsed[index] else 'Failed'}
#     """

#     print(dem)
#     print("-"*50)
# 
# names = []
# addresses = []

# names.append("Ram") # Ask for Name 
# names.append("Shyam") # Ask for Name 

# addresses.append("Ayodhya") # Ask for Address
# addresses.append("Delhi") # Ask for Address


# # for item in zip(names, addresses):
# #     # 
# #     a, b = item
# #     print(item)
# #     print(a,b)

# names.insert(1, "Keshab")

# print(names)

# value = names.pop(1)
# print(names, value)

# check = "Ram"
# if check in names:
#     breakpoint()
#     names.remove(check)
# print(names)
# Ram
# Keshab
# Shyam

# WAP
# Ask for name, marks, at least 4 students
# make a pass list and fail list iterating over the items 

# [("Ram", 50, "Pass"),
# ("Shyam", 40, "Fail")]

# name, marks, result = ("Ram", 50, "Pass")


# name_list , marks_list = [], []
# for _ in range(4):
#     name_list.append(input("Enter Name \n"))
#     marks_list.append(float(input("Enter Marks \n")))


# result_list = []
# for name, marks in zip(name_list, marks_list):
#     result_list.append(
#         (
#             name,
#             marks,
#             "Pass" if marks >= 50 else "Fail"
#         )
#     )

# # print(result_list)

# # [("Ram", 50, "Pass")]

# passed_students = list(filter(lambda x: x[2] == "Pass", result_list))
# print(passed_students)

# passed_students.sort(key=lambda x : x[1], reverse=True) # In place sorting

# # sorted() -> New Sorted Object -> List
# print(passed_students)

# 


list_of_persons = ["Ram", "Shyam", "Rita", "Love"]

# for i in list_of_persons:
#     i

mod_list = [f"Person : {i}" for i in list_of_persons if "o" in i.lower()] # This is list comprehension with condition

print(mod_list)


