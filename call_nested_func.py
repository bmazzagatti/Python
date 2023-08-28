#!/usr/bin/env python3

def shipping_cost(cart):
    if cart < 50:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

shipping_cost(40)
shipping_cost(100)            