#!/usr/bin/env python3

def decode_message(message: str, shift: int) -> str:
    decoded = ""
    shift = shift % 26
    for ch in message:
        if ch == " ":
            decoded += " "
        else:
            decoded += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
    return decoded
