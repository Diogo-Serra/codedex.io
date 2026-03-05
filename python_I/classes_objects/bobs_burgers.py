#!/usr/bin/env python3

class Restaurant():
    name: str = None
    category: str = None
    rating: float = None
    delivery: bool = None


bobs_burgers = Restaurant()
bobs_burgers.name = "Bob\'s Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False
test1_burgers = Restaurant()
test1_burgers.name = "Bob\'s Burgers 2"
test1_burgers.category = "American Diner"
test1_burgers.rating = 4.7
test1_burgers.delivery = False
test2_burgers = Restaurant()
test2_burgers.name = "Bob\'s Burgers 3"
test2_burgers.category = "American Diner"
test2_burgers.rating = 4.7
test2_burgers.delivery = False
print(vars(bobs_burgers))
print(vars(test1_burgers))
print(vars(test2_burgers))
