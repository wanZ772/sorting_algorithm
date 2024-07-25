from time import time
init_time = time()
# raw_data = [10, 14, 28, 11, 7, 16, 30, 50, 25, 18]
raw_data = [17, 92, 55, 31, 74, 8, 62, 49, 23, 37, 82, 46, 11, 69, 28, 91, 14, 72, 43, 19, 67, 29, 58, 83, 7, 64, 38, 13, 79, 53, 26, 89, 61, 16, 71, 44, 34, 97, 22, 77,73, 59, 14, 82, 61, 46, 38, 97, 23, 55, 74, 49, 65, 31, 44, 8, 86, 19, 68, 7, 88, 26, 71, 5, 34, 91, 53, 29, 56, 37, 79, 22, 64, 47, 1, 94, 16, 43, 77, 11, 49, 82, 38, 32, 72, 11, 94, 61, 24, 86, 53, 29, 43, 16, 34, 19, 77, 5, 82, 2, 55, 37, 83, 8, 28, 26, 69, 59, 14, 76, 1, 64, 47, 71, 49, 23, 58, 46, 97, 7, 88, 44, 22, 94, 65, 41, 74, 13, 79, 17, 92, 55, 31, 74, 8, 62, 49, 23, 37, 82, 46, 11, 69, 28, 91]

def selection(raw_data):
    for i in range(len(raw_data) - 1):
        min = i
        for j in range(i, len(raw_data)):
            if raw_data[j] < raw_data[min]:
                min = j
        if min != i:
            raw_data[i], raw_data[min] = raw_data[min], raw_data[i]
    return raw_data
print(f"Sorted: {selection(raw_data)}")
print(f"Time: {time() - init_time}")
