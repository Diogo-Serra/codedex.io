#!/usr/bin/env python3

class BankAccount():
    def __init__(
        self,
        first_name,
        last_name,
        account_id,
        account_type,
        pin,
        balance,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, ammount):
        self.balance -= ammount

    def display_balance(self):
        print(self.balance)
