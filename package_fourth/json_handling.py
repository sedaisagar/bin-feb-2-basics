import json

with open("sample.json", "r") as fptr:

    json_objs = json.load(fptr)



with open("sample.json", "w") as fptr:
    my_obj = [ 
        *json_objs,
        {
            "name":"Sagar" ,
            "age":55,
        }
        ,{
            "name":"Rita" ,
            "age":56,
        },{
            "name":"Sita" ,
            "age":46,
        }
    ]
    json.dump(my_obj, fptr)
