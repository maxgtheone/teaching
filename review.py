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

# Any greeting function has to look like this
# def any_greeting_function(arg: str) -> str:
#      do anything here

# F-strings
random_var = 'max'
good_string = f"{random_var} hello"  # will give string -> "max hello"
bad_string = random_var + " hello"  # NO string + string + another_string -> BAD


def positive_greeting(name: str) -> str:
    return f'howdy, {name}'


def negative_greeting(name: str) -> str:
    return f"fuck you {name}"


def print_greeting(greeting_fn: Callable[[str], str], name: str) -> None:
    print(greeting_fn(name))


print_greeting(greeting_fn=negative_greeting, name='max')
print_greeting(greeting_fn=positive_greeting, name='max')


def greeting(greeting_type: str, name: str) -> None:
    greet = ""
    if greeting_type == 'positive':
        greet = f"howdy, {name}"
    elif greeting_type == 'negative':
        greet = f"fuck you {name}"
    print(greet)

## Bad because you have to edit the function to make more modifications -> violates Open/Closed Principal which says your code must be 'Open for extension, and closed for modification'


# Anonymous functions
# These are functions that don't have a formal definition, but can be used in the local scope of your code, kind of like 'throwaway functions'

add_two = lambda x: x + 2 # lambda == anonymous function
answer = add_two(3) # this gives you 5

final_list_comprehension = [add_two(i) for i in range(3)]






