#!/usr/bin/env python3

def pick_voucher(vouchers: list, delays: list, max_wait: int) -> str:
    best_value = 0
    index = -1
    for i, (voucher, delay) in enumerate(zip(vouchers, delays)):
        print(f"Index: {i} Price: {voucher} Delay: {delay}")
        if delay < max_wait:
            if index == -1 or best_value < (voucher / delay):
                best_value = voucher / delay
                index = i
    return index


def tester() -> None:
    vouchers = [50, 120, 20]
    delays = [2, 4, 1]
    max_wait = 3
    index = pick_voucher(vouchers, delays, max_wait)
    print(index)


tester()
