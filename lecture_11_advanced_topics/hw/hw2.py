"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10

"""
from __future__ import annotations


class Discount:
    """The strategy interface declares operations common to all
    supported versions of some algorithm. The context uses this
    interface to call the algorithm defined by the concrete strategies.

    """

    @classmethod
    def __init_subclass_(cls):
        if not hasattr(cls, "discount"):
            raise NotImplementedError(
                f"Class {cls} lacks required discount class attribute"
            )

    @staticmethod
    def final_price(order: Order) -> int:
        return order.price - order.price * order.discount_program.discount


class NoDiscount(Discount):

    discount = 0


class MorningDiscount(Discount):

    discount = 0.5


class ElderDiscount(Discount):

    discount = 0.9


class Order:
    """Gets the order price and discount program.
    When calling the final_price method, the order price is returned.

    Args:
        price: The order price.
        discount_program: The desired discount program.

    Attributes:
        price: The order price.
        discount_program: The desired discount program.

    """

    def __init__(self, price, discount_program):
        self.price = price
        self.discount_program = discount_program

    def final_price(self):
        return self.discount_program.final_price(self)


if __name__ == "__main__":
    order1 = Order(100, NoDiscount)
    # print(order1.final_price())
    # print(order1.final_price())

    order1.discount_program = MorningDiscount

    # order2 = Order(100, "morning_discount")
    # print(order1.final_price())

    order3 = Order(100, ElderDiscount)
    # print(order3.final_price())
