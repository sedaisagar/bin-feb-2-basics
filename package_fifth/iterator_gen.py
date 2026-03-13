# Generator Function 
# import time


# def generate_upto(num=5):
#     while num > 0:
#         print(f"Executing For #{num}")
#         time.sleep(1)
#         yield num
#         print(f"Executed For #{num}")
#         num -= 1



# generated_object = generate_upto()

# item_1 = next(generated_object)
# print(item_1)


class Counter:
    def __init__(self, start, end):
        # super().__init__(start, end)
        self.current = start
        self.end = end

    def __iter__(self):
        return self # Returns the object itself

    def __next__(self):
        if self.current > self.end:
            raise StopIteration # Stops the iteration
        else:
            self.current += 1
            return self.current - 1 # Returns the current item


counter = Counter(1, 5)
# for num in counter:
#     print(num) # Output: 1, 2, 3, 4, 5

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# 
# print(next(counter))