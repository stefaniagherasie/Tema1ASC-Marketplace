"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""
from threading import Lock

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """

        self.queue_size_per_producer = queue_size_per_producer
        self.prod_count = 0
        self.cart_count = 0

        self.products = {}      # key: prod_id, value: list of products
        self.carts = {}         # key: cart_id, value: list of products

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """

        self.prod_count = self.prod_count + 1
        self.products[self.prod_count] = []

        return self.prod_count

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """

        temp = self.products[producer_id]
        if len(temp) < self.queue_size_per_producer:
            print(self.products[producer_id])
            self.products[producer_id].append(product)
            print(self.products[producer_id])
            return True

        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.cart_count = self.cart_count + 1
        self.carts[self.cart_count] = []

        return self.cart_count

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """

        for key in self.products.keys():
            if product in self.products[key]:
                #print(self.carts[1])
                self.carts[cart_id].append(product)
                #print(self.carts[1])
                self.products[key].remove(product)

                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """

        for key in self.products.keys():
            if product in self.products[key]:
                self.carts[cart_id].remove(product)
                self.products[key].append(product)
                break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """

        order = self.carts[cart_id]

        #print(order)
        #self.carts.pop(cart_id)
        return order
