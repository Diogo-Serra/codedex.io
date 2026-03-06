import unittest


class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, item):
        return self.menu.get(item)

    def add_item(self, item, price):
        self.menu[item] = price


class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.coffee_menu = CoffeeMenu()

    def test_get_price_existing_item(self):
        """A latte should cost $2.75."""
        self.assertEqual(self.coffee_menu.get_price('latte'), 2.75)

    def test_get_price_non_existing_item(self):
        """Requesting a non-existent item should return None."""
        self.assertIsNone(self.coffee_menu.get_price('matcha'))

    def test_add_item(self):
        self.coffee_menu.add_item('mocha', 3.50)
        self.assertEqual(self.coffee_menu.get_price('mocha'), 3.50)


if __name__ == '__main__':
    unittest.main()
