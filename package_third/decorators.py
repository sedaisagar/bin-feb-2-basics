def ma_dec(param1, param2):

    def inner(func):

        def inner1(*args, **kwargs):
            print("Inner1 Call")
            return func(*args, **kwargs)

        print("Inner Call")
        return inner1

    print(f"Param1 : {param1}, Param2 : {param2}")
    print("Main Call")

    return inner

@ma_dec(123, 456)
def chk(*args, **kwargs):
    print(args, kwargs)

chk(11,22,33)