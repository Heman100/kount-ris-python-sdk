#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the Kount python sdk project (https://bitbucket.org/panatonkount/sdkpython)
# Copyright (C) 2017 Kount Inc. All Rights Reserved.

__author__ = "Yordanka Spahieva"
__version__ = "1.0.0"
__maintainer__ = "Yordanka Spahieva"
__email__ = "yordanka.spahieva@sirma.bg"
__status__ = "Development"


class CartItem(object):
    """A class that represents a shopping cart item.
    kwargs -
        product_type - the product type
        item_name - name of the item
        description - description
        quantity - quantity
        price - the price of the item
    """
    def __init__(self, product_type="", item_name="", description="", quantity="", price=""):
        "Constructor for a cart item."
        self.product_type = product_type
        self.item_name = item_name
        self.description = description
        self.quantity = quantity
        self.price = price

    def to_string(self):
        "String representation of this shopping cart item"
        cart = "Product Type: %s\nItem Name: %s\nDescription: %s\nQuantity: %s\nPrice: %s\n"%(
        self.product_type, self.item_name, self.description, self.quantity, self.price)
        return cart


if __name__ == "__main__":
    c = CartItem()
    c.product_type = 666
    c.item_name = 666
    c.description = 666
    c.quantity = 666
    c.price = 666
    print(c.to_string())