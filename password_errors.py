#!/usr/bin/env python3

class PasswordError(Exception): #PasswordError is the 'supertype'
    """Base class for exceptions in this module.""" # no implementation
    pass    # extends exeption
#-------------------------------------------------------
# below are 3 concrete causes why a password is rejected
class TrivialPasswordError(PasswordError):  # child of PasswordError
    """Passwords that are too Trivial like: 'password'"""
    def __init__(self, msg):
        super().__init__("Trivial Password:" + msg)


class PasswordLengthError(PasswordError):
    """Passwords that do not meet certain length criteria"""
    def __init__(self, msg, length):    # includes length of pw in the exception payload
        super().__init__(msg)   # calls the superclass
        self.length = length

    def get_length(self):
        return self.length


class RepetetiveError(PasswordError):
    """Passwords that have repetitive characters"""
    def __init__(self, msg):
        super().__init__(msg)   # extension of the pw error one-to-one, more descriptive name (RepetetiveError)