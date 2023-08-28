#!//usr/bin/env python3


import time

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
        time.sleep(1)
    print("Happy New Year!")

do_countdown(10)