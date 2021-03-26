"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """

        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        Thread.__init__(self, **kwargs)


    def add_product(self, cart_id, product, quantity):
        for i in range(quantity):
            tmp = self.marketplace.add_to_cart(cart_id, product)
            while tmp is False:
                time.sleep(self.retry_wait_time)
                tmp = self.marketplace.add_to_cart(cart_id, product)


    def remove_product(self, cart_id, product, quantity):
        for i in range(quantity):
            tmp = self.marketplace.remove_from_cart(cart_id, product)
            while tmp is False:
                time.sleep(self.retry_wait_time)
                tmp = self.marketplace.remove_from_cart(cart_id, product)

    def run(self):
        for cart in self.carts:
            cart_id = self.marketplace.new_cart()

            for request in cart:
                order = request["type"]
                product = request["product"]
                quantity = request["quantity"]

                if order == "add":
                    self.add_product(cart_id, product, quantity)
                elif order == "remove":
                    self.remove_product(cart_id, product, quantity)

            self.marketplace.place_order(cart_id)
