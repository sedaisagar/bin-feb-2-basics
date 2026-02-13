# Python sets

# number_sets = {1,3,5,6,3} #or set({1,2,3,4,3})

# print(number_sets)


# even_numbers = {0,2,4,6,8,}
# even_numbers.add(10)
# odd_numbers = {0,1,3,5,7,9,}
# odd_numbers.remove(0)


# print(even_numbers.union(odd_numbers))
# print(odd_numbers.difference(even_numbers))

# locked_set = frozenset(even_numbers)

# # locked_set.

love = lambda x : x+5


gens = (love(i) for i in range(5))

print(gens)

# print(next(gens))
# print(next(gens))
# print(next(gens))
# print(next(gens))
# print(next(gens))

print("*"*50)
for i in gens:
    if i == 6:
        exit(50)
        continue
    if i ==9:
        break
    print(i)
else:
    print("Nothing is remained")
