def selection_sort(data):
    for i in range(0, len(data)):
        m = i
        for j in range(i+1, len(data)):
            if data[j] < data[m]:
                m = j
        data[i], data[m] = data[m], data[i]

def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
            j -= 1

def insertion_sort_2(data):
    for i in range(1, len(data)):
        j = i
        temp = data[j]
        while j > 0 and temp < data[j-1]:
            data[j] = data[j-1]
            j -= 1
        data[j] = temp

def merge_sort(data):

    copy = [0] * len(data)

    def merge(low, mid, high):
        for a in range(low, high + 1):
            copy[a] = data[a]
        i, j = low, mid+1
        for k in range(low, high+1):
            if i > mid:
                data[k] = copy[j]
                j += 1
            elif j > high:
                data[k] = copy[i]
                i += 1
            elif copy[i] < copy[j]:
                data[k] = copy[i]
                i += 1
            else:
                data[k] = copy[j]
                j += 1
    
    def sort(low, high):
        if (high - low) <= 0:
            return
        mid = low + (high - low) // 2
        sort(low, mid)
        sort(mid+1, high)
        merge(low, mid, high)

    sort(0, len(data) - 1)

from random import shuffle
def quick_sort(data):

    def partition(low, high):
        i, j = low, high + 1
        while True:
            while True:
                i += 1
                if i == high or data[i] >= data[low]:
                    break
            while True:
                j -= 1
                if j == low or data[j] <= data[low]:
                    break
            if i >= j:
                break
            data[i], data[j] = data[j], data[i]
        data[low], data[j] = data[j], data[low]
        return j
    
    def sort(low, high):
        if low >= high:
            return
        pivot = partition(low, high)
        sort(low, pivot - 1)
        sort(pivot + 1, high)
    
    #shuffle(data)
    sort(0, len(data) - 1)

def is_sorted(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            return False
    return True

from timeit import timeit
from random import randint
data = list()
for n in range(800000):
    data.append(randint(0, 1000000))

print("Sorting...")
exec_time = timeit('quick_sort(data)', number=1, globals=globals())
print(f"Execution time: {exec_time} seconds")
print(f"Is sorted: {is_sorted(data)}")