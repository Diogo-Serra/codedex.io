#!/usr/bin/env python3

def pick_voucher(vouchers: list, delays: list, max_wait: int) -> str:
    for voucher in vouchers:
        print(voucher)
        print(delays)
        print(max_wait)


def tester() -> None:
    vouchers: list = [100, 200, 300, 400]
    delays: list = [1, 2, 3, 4]
    max_wait: int = 2
    pick_voucher(vouchers, delays, max_wait)


tester()
