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
    
    def med3_partition(low, high):
        insertion(low, low + 2)
        data[low], data[low+1] = data[low+1], data[low]
        data[low+2], data[high] = data[high], data[low+2]
        i, j = low + 1, high
        v = data[low]
        while True:
            while True:
                i += 1
                if data[i] >= v:
                    break
            while True:
                j -= 1
                if data[j] <= v:
                    break
            if i >= j:
                break
            data[i], data[j] = data[j], data[i]
        data[low], data[j] = data[j], data[low]
        return j
    
    def insertion(low, high):
        for i in range(low + 1, high + 1):
            j = i
            temp = data[j]
            while j > low and temp < data[j-1]:
                data[j] = data[j-1]
                j -= 1
            data[j] = temp
    
    def sort(low, high):
        if high - low <= 15:
            insertion(low, high)
            return
        pivot = med3_partition(low, high)
        sort(low, pivot - 1)
        sort(pivot + 1, high)
    
    shuffle(data)
    sort(0, len(data) - 1)

def quick_sort_3way(data):

    def partition(low, high):
        lt = low
        i = low + 1
        gt = high
        v = data[low]
        while i <= gt:
            if data[i] < v:
                data[lt], data[i] = data[i], data[lt]
                lt += 1
                i += 1
            elif data[i] > v:
                data[i], data[gt] = data[gt], data[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    def sort(low, high):
        if low >= high:
            return
        lt, gt = partition(low, high)
        sort(low, lt - 1)
        sort(gt + 1, high)
    
    shuffle(data)
    sort(0, len(data) - 1)

def is_sorted(data):
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            return False
    return True

from timeit import timeit
from random import randint
data = list()
for n in range(100000):
    data.append(randint(0, 100))

print("Sorting...")
exec_time = timeit('quick_sort_3way(data)', number=1, globals=globals())
print(f"Execution time: {exec_time} seconds")
print(f"Is sorted: {is_sorted(data)}")