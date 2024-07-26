# Time: O(n^2)
# Space: O(1)

from random import randint
from time import time

raw_data = []

test_data = [7,4,5,2]

def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))

def insertion():
    for i in range(1, len(raw_data)):
        j = i
        while j > 0:
            print(f"point: {j} --> {raw_data}")
            if raw_data[j-1] > raw_data[j]:
                raw_data[j], raw_data[j-1] = raw_data[j-1], raw_data[j]
            j -= 1

random_generator(10)
print(f"Raw data: {raw_data}")
start = time()
insertion()
finish = time()
print(f"Sorted data: {raw_data}")
print(f"Time: {finish-start}")