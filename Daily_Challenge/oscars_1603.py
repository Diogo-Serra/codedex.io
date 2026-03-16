#!/usr/bin/env python3

def oscar_pool(predictions):
    winners = (
        "One Battle After Another",
        "Michael B. Jordan",
        "Jessie Buckley",
        "Paul Thomas Anderson",
    )

    best_name = None
    best_correct = -1
    is_tie = False

    for friend in predictions:
        name = friend[0]
        picks = friend[1:]

        correct = 0
        for i in range(4):
            if picks[i] == winners[i]:
                correct += 1

        if correct > best_correct:
            best_correct = correct
            best_name = name
            is_tie = False
        elif correct == best_correct:
            is_tie = True

    if is_tie:
        return "Tie"
    return best_name


def test_predictions():
    friends_predictions = [
        ["@sonny", "One Battle After Another", "Michael B. Jordan",
         "Jessie Buckley", "Ryan Cooger"],
        ["@brit896", "Marty Supreme", "Timothée Chalamet",
         "Jessie Buckley", "Josh Safdie"],
        ["@tylerwhit", "Sinners", "Michael B. Jordan",
         "Rose Byrne", "Paul Thomas Anderson"]
    ]
    print(oscar_pool(friends_predictions))


if __name__ == '__main__':
    test_predictions()
