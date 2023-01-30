# Give me an example of a higher order function

from typing import Callable

buy_strategy = Callable[[float], bool]


def first_buy_strategy(price: float):
    if price < 100:
        should_buy = True
    else:
        should_buy = False
    return should_buy


def second_buy_strategy(price: float):
    if price < 50:
        should_buy = True
    else:
        should_buy = False
    return should_buy


def order_amount(should_buy: buy_strategy, price: float):
    qty = 0
    if should_buy(price):
        qty = 10
    return qty


order_amount(first_buy_strategy, 75)

#Partial functions from functools

from functools import partial
import functools

order_from_first_strategy = functools.partial(order_amount, first_buy_strategy)

order_from_first_strategy(75)
# import package_example
# from directory_example import review
# print(review.add_one(20))

