# List Comprehensions
# Efficient way of looping, only use for simple loops,
# returns lists and what it can return is up to you but usually an output of the thingy

test_list_comprehension = [i for i in range(3)]  # -> returns [0, 1, 2]

# For loop equivalent
return_list = []
for i in range(3):
    return_list.append(i)


def add_one(number: int) -> int:
    return number + 1


# Create a list comprehension that utilizes the add_one function and returns a list [1,2,3]

example_two_list_comprehension = [add_one(i) for i in range(3)]  # -> returns [1,2,3]


def fn() -> int:
    return 1


example_three_list_comprehension = [fn() for _ in range(3)]  # -> returns [1,1,1]


## args and kwargs

def args_fn(*args: int) -> int:
    # what does args look like in the function -> list of integers
    return args[0]


# how can I call this function?

args_fn(4, 3, 2, 5)  # returns -> 4
# unpacking using *
args_fn(*[4, 3, 2, 1])  # equivalent to args_fn(4, 3, 2, 5)


# kwargs
def kwargs_fn(**kwargs):
    # kwargs = {'name':'max',
    #           'age': 27}
    return kwargs['name']


kwargs_fn(name='max', age=27)


def greeting(name: str, age: int, favorite_food: str) -> None:
    print(f"Hi {name}, you are {age} years old and your favorite food is {favorite_food}")


greeting('max', 27, 'pizza')  # implicit calling
greeting(name='max', age=27, favorite_food='pizza')  # explicit calling

# Higher order functions
# These are functions that take other functions as inputs

from typing import Callable  # this is the 'function' type

# The structure of the Callable type is Callable[[input_types], output_types]
greeting_function = Callable[[str], str]

#Any greeting function has to look like this
# def any_greeting_function(arg: str) -> str:
#      do anything here

def positive_greeting():
    ...