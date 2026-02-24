def get_numeric_value():
    return int(input("Enter your age \t"))

def printer(number_of_times, people=[]):
    if number_of_times == 0:
        print(f"Stopping the recursion #{number_of_times}!")
        
        number_of_people = len(people)
        age_sum = sum(i["age"] for i in people)
        return people, age_sum / number_of_people

    while number_of_times > 0:
        print(f"I'm getting printed for #{number_of_times}")
        people.append({
            "name":input("Enter your name \t"),
            "age": get_numeric_value(),
        })
        return printer(number_of_times-1, people)

people, mean_age = printer(5)

print(people, mean_age)



