#!/usr/bin/env python3

menu = [
    '🍔 Cheeseburger',
    '🍟 Fries',
    '🥤 Soda',
    '🍦 Ice Cream',
    '🍪 Cookie']


def get_item(item_number):
    return menu[item_number - 1]
