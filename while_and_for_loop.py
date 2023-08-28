#!//usr/bin/env python3

"""this program prints downloading files one at a time by importing the 'time' module using a 'for' AND 'while' loop"""
import time

def display_progress(total_files):
    for i in range(total_files + 1):
        print(f"Downloading file {i} out of {total_files}")
        time.sleep(1)

display_progress(5)
print("Complete!")