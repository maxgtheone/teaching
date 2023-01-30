# call in function that is passed as an argument

from person import Person


def lame_intro(first_name: str, last_name: str, age: int) -> None:
    print(f"Attention Duelists, {first_name} {last_name} has entered the arena at age {age}!")


def cool_intro(first_name: str, last_name: str, age: int) -> None:
    print(f"Hey, this is {first_name} {last_name}, I'm only {age}, I'm drowning lol")


Ray = Person(first_name="Ray", last_name="Greenberg", age=30, introduction=cool_intro)
