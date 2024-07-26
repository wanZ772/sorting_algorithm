# Time: O(n log n)
# Space: O(log2n)

from time import time
from random import randint

raw_data = []

def random_generator(target):
    for i in range(target):
        raw_data.append(randint(0, target))
def merge(data):
    n = len(data)

    if n == 1:
        return data
    else:
        mid = n // 2
        left = data[:mid]
        right = data[mid:]
        
        left = merge(left)
        right = merge(right)

        sorted_data = []

        left_point, right_point, i = 0, 0, 0

        while left_point < len(left) and right_point < len(right):
            if left[left_point] < right[right_point]:
                sorted_data.append(left[left_point])
                left_point += 1
            else:
                sorted_data.append(right[right_point])
                right_point += 1
        while left_point < len(left):
            sorted_data.append(left[left_point])
            left_point += 1
        while right_point < len(right):
            sorted_data.append(right[right_point])
            right_point += 1
        return sorted_data

random_generator(10)
print(f"Raw data: {raw_data}")
start = time()
sorted_ = merge(raw_data)
finish = time()
print(f"Sorted data: {sorted_}")
print(f"Time: {finish-start}")