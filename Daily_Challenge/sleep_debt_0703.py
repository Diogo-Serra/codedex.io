def calculate_sleep_debt(planned, actual):
    debts = [max(0, p - a) for p, a in zip(planned, actual)]

    total_debt = sum(debts) + 1  # +1 for Daylight Savings

    longest_streak = 0
    current_streak = 0
    for debt in debts:
        if debt > 0:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    return total_debt, longest_streak


# Example 1: Sonny
planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]
print(calculate_sleep_debt(planned, actual))  # (8.0, 2)


# Example 2: Asiqur
planned = [6, 6, 6, 6, 6, 8, 8]
actual = [5, 7, 2.5, 5, 5.5, 6, 4]
print(calculate_sleep_debt(planned, actual))  # (13.0, 5)
