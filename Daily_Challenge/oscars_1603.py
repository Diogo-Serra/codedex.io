#!/usr/bin/env python3

def oscar_pool(predictions):
    winners = {
        "Best Picture:": "One Battle After Another",
        "Best Actor:": "Michael B. Jordan",
        "Best Actress:": "Jessie Buckley",
        "Best Director:": "Paul Thomas Anderson"
    }
    print(type(winners))
    print(winners["Best Actor:"])


oscar_pool("One Battle After Another")
