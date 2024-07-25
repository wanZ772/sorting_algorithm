from random import randint
from time import time

raw_data = []

test_data = [7,4,5,2]

def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))
def insertion():
    target_point = 0
    for i in raw_data:
        for j in range(len(raw_data) - 1):
            # print(f"target point: {target_point} --> {raw_data}")
            if raw_data[target_point] > raw_data[j+1]:
                raw_data[target_point], raw_data[j+1] = raw_data[j+1], raw_data[target_point]
            target_point += 1
        target_point = 0

random_generator(1000)
print(f"Raw data: {raw_data}")
start = time()
insertion()
finish = time()
print(f"Sorted data: {raw_data}")
print(f"Time: {finish-start}")