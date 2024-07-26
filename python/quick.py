# time : O(n log n)
# Space: O(n)

from time import time
from random import randint

raw_data = []
def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))

def quick(data):
    n = len(data)

    if n <= 1:
        return data
    else:
        mid = data[-1]
        left, right = [], []
        for i in data[:-1]:
            if i < mid:
                left.append(i)
            else:
                right.append(i)
        left = quick(left)
        right = quick(right)
        return left + [mid] + right

random_generator(10)
print(f"Raw data: {raw_data}")
start = time()
sorted_ = quick(raw_data)
finish = time()
print(f"Sorted data: {sorted_}")
print(f"Time: {finish-start}")