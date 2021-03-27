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
        self.carts = {}         # key: cart_id, value: list of (product, producer)
        self.lock = Lock()

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """

        with self.lock:
            # Give the producer an id
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

        tmp = self.products[producer_id]
        if len(tmp) <= self.queue_size_per_producer:
            # Add the product to the buffer, if there is space
            self.products[producer_id].append(product)
            return True

        # If the buffer is full, make consumer wait and try later
        return False


    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.lock:
            # Give the cart an id
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

        for producer_id in self.products:
            if product in self.products[producer_id]:
                # Find the product
                tmp = (product, producer_id)

                # Add the product to the cart and remove it from the producer list
                self.carts[cart_id].append(tmp)
                self.products[producer_id].remove(product)
                return True

        # If the product was not found, make consumer wait and try later
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """

        # Search in cart for the product
        for tmp in self.carts[cart_id]:
            current_prod = tmp[0]
            producer_id = tmp[1]

            if product == current_prod:
                # Remove the product from the cart and add it to the producer list
                self.carts[cart_id].remove(tmp)
                self.products[producer_id].append(product)
                return


    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """

        order = []
        # From the list of product from the order
        for product in self.carts[cart_id]:
            order.append(product[0])

        # Remove the cart from the carts list
        self.carts.pop(cart_id)

        return order
