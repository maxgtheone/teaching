# List Comprehensions
# Efficient way of looping, only use for simple loops,
# returns lists and what it can return is up to you but usually an output of the thingy

test_list_comprehension = [i for i in range(3)]

# For loop equivalent
return_list = []
for i in range(3):
    return_list.append(i)


def add_one(i: int) -> int:
    return i + 1

#Create a list comprehension that utilizes the add_one function and returns a list [1,2,3]

example_two_list_comprehension = [add_one(i) for i in range(3)]
