# student = {
#     # "name":"Ram Bdr",
#     # "age":20,
#     # "address":"Kathmandu",
# } #or dict()

# # print(student["address"]) # Accessing value in key within dict
# print(student.get("address", "No Value Found")) # Accessing value in key within dict
# student["address"] = "Pokhara" # Assigning value in key within dict
# print(student["address"])

# # student.setdefault("name","No name")
# # student.setdefault("name","Keshab")

# student.update(name="No name")
# print(student)

# student.update(name="Keshab")
# print(student)


# students = []


# for _ in range(3):
#     print("-"*50)
#     students.append(
#         {
#             "name": input("Enter name of student \n"),
#             "age": int(input("Enter age of student \n")),
#             "address": input("Enter address of student \n"),
#         }
#     )
#     print("-"*50)


# # "ram" in "ram thapa"
# while True:
#     name = input("Enter the name to filter out \n")

#     result = list(filter(lambda x: name.lower() in x["name"].lower(), students))

#     print(result)

#     if input("Do you want to break herein , y/n ? \t ") == "y":
#         print("Exiting from filter shell!------------>>>")
#         break
#     print("*"*50)
    
# while True:
#     key = input(f"Enter the sort basis, {" ".join(list(students[0].keys()))}")

#     splits = key.split("-") #-> List of splitted strings on the basis of provided char
    
#     print(f"Splitted Chars {splits}")

#     if len(splits) > 1:
#         print("Applying desc sort")
#         result = list(sorted(students,key=lambda x: x[splits[1]], reverse=True))
#     else:
#         print("Applying asc sort")
#         result = list(sorted(students,key=lambda x: x[key]))
#         # 
#     print(result)

#     if input("Do you want to break herein , y/n ? \t ") == "y":
#         print("Exiting from filter shell!------------>>>")
#         break
#     print("*"*50)


# 
# map() -> Transform the original data

# [{"name":""}, {"name":""}]


students = [
    {"name":"Rita", "age":23, "address":"Kapan"},
    {"name":"Ritaa", "age":22, "address":"Kapans"},
    {"name":"Ritas", "age":21, "address":"Kapano"},
    {"name":"Ritao", "age":25, "address":"Kapand"},
]

transformed_students = list(map(lambda x: (x["name"], x["age"], x["address"]), students))

print(transformed_students)



# Nested Dictionary
# {
#     "person": {
#         "name":"Ram",
#         "age":"20",
#     },
#     "address":{
#         "permanent_address":{
#             "state":"Bagmati",
#         },
#         "temporary_address":{
#             "zip":44600,"state":"Bagmati",
#             "zip":44600,
#         }
#     }
# }