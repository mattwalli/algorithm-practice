def selection_sort(data):
    for i in range(0, len(data)):
        m = i
        for j in range(i+1, len(data)):
            if data[j] < data[m]:
                m = j
        data[i], data[m] = data[m], data[i]

def is_sorted(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            return False
    return True

from timeit import timeit
from random import randint
data = list()
for n in range(10000):
    data.append(randint(0, 1000000))

exec_time = timeit('selection_sort(data)', number = 1, globals=globals())
print(f"Execution time: {exec_time} seconds")
print(f"Is sorted: {is_sorted(data)}")