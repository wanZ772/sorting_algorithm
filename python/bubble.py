# time : O(n^2)
# Space: O(1)

from time import time
from random import randint

raw_data = []
def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))

def bubble():
    for i in raw_data:
        for j in range(len(raw_data) - 1):
            if raw_data[j] > raw_data[j+1]:
                raw_data[j], raw_data[j+1] = raw_data[j+1], raw_data[j]

random_generator(10)
print(f"Raw data: {raw_data}")
start = time()
bubble()
finish = time()
print(f"Sorted data: {raw_data}")
print(f"Time: {finish-start}")