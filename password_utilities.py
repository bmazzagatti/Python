#!/usr/bin/env python3

import password_errors  # imports entire password_errors.py library


def check_trivial(password):    # check function
    bad = ["password", "p@ssword", "passw0rd", "p@ssw0rd"]
    if password.lower() in bad:
        raise password_errors.TrivialPasswordError(password)


def check_length(password):    # check function
    min_length = 10
    length = len(password)
    if length < min_length:
        raise password_errors.PasswordLengthError("Too short", length) # if checkfunction fails, raise corresponding exception type


def check_duplicates(password):    # check function
    removedupes = set(password)
    if len(removedupes) < len(password):
        raise password_errors.RepetetiveError("Repetetive Characters Exist")