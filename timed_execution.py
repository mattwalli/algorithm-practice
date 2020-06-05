import random

rand_nums = list()
for n in range(1000000):
    rand_nums.append(random.randint(-1000000, 1000000))

def test_function():
    rand_nums.sort()

import timeit
exec_time = timeit.timeit('test_function()', number = 1, globals=globals())
print(f"Execution time: {exec_time} seconds")

# built in sort: ~0.34sec @ 1M grows at nlogn