import math
import matplotlib 
import matplotlib.pyplot as plt
import time
import random


class QuickSort:
    def __init__(self, arr):
        self.arr = arr
        self.start = 0
        self.end = 0


    def quickSortRecursive(self, arr, beg, end, pivotMethod):
        if end - beg < 2:
            return

        pivotIndex = pivotMethod(arr, beg, end)
        pivot = arr[pivotIndex]
        arr[pivotIndex], arr[end - 1] = arr[end - 1], arr[pivotIndex]

        i = beg
        
        for j in range(beg, end - 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                
        arr[i], arr[end - 1] = arr[end - 1], arr[i]

        self.quickSortRecursive(arr, beg, i, pivotMethod)
        self.quickSortRecursive(arr, i + 1, end, pivotMethod)

        return arr

    def pivotFirstElement(self, arr, beg, end):
        return beg

    def pivotMiddleElement(self, arr, beg, end):
        return (beg + end - 1) // 2

    def pivotLastElement(self, arr, beg, end):
        return end - 1

    def pivotRandomElement(self, arr, beg, end):
        return math.floor(beg + (end - beg) * 0.5)

    def pivotMedianFirstMiddleLastElement(self, arr, beg, end):
        first = arr[beg]
        middle = arr[(beg + end - 1) // 2]
        last = arr[end - 1]
        median = sorted([first, middle, last])[1]
        return arr.index(median, beg, end)
    
    def pivotMedianThreeRandomElement(self, arr, beg, end):
        if end - beg < 3:
            return arr[beg]
        
        indices = random.sample(range(beg, end), 3)
        
        elements = [arr[i] for i in indices]
        elements.sort()
        median = elements[1]
        return median
                

    def firstElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotFirstElement)

    def middleElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotMiddleElement)

    def lastElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotLastElement)

    def randomElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotRandomElement)

    def medianFirstMiddleLastElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotMedianFirstMiddleLastElement)

    def medianThreeRandomElementPivot(self):
        return self.quickSortRecursive(self.arr, 0, len(self.arr), self.pivotMedianThreeRandomElement)
    
    
    def initTime(self):
        self.start = time.time()

    def endTime(self):
        self.end = time.time()
        return self.end - self.start


# arr = [6, 3, 5, 3, 3, 6, 2, 8, 9, 4, 1]

arr = [random.randint(1, 100) for _ in range(1000)]

qs = QuickSort(arr)

qs.initTime()
qs.firstElementPivot()
firstElementTime = qs.endTime()

qs.initTime()
qs.middleElementPivot()
middleElementTime = qs.endTime()

qs.initTime()
qs.lastElementPivot()
lastElementTime = qs.endTime()

qs.initTime()
qs.randomElementPivot()
randomElementTime = qs.endTime()

qs.initTime()
qs.medianFirstMiddleLastElementPivot()
medianFirstMiddleLastElementTime = qs.endTime()

# qs.initTime()
# qs.medianThreeRandomElementPivot()
# medianThreeRandomElementTime = qs.endTime()


averageFirstElementTime = 0
averageMiddleElementTime = 0
averageLastElementTime = 0
averageRandomElementTime = 0
averageMedianFirstMiddleLastElementTime = 0
averageMedianThreeRandomElementTime = 0

for i in range(100):
    arr = [random.randint(1, 10000) for _ in range(1000)]
    
    qs = QuickSort(arr)

    qs.initTime()
    qs.firstElementPivot()
    averageFirstElementTime += qs.endTime()

    qs.initTime()
    qs.middleElementPivot()
    averageMiddleElementTime += qs.endTime()

    qs.initTime()
    qs.lastElementPivot()
    averageLastElementTime += qs.endTime()

    qs.initTime()
    qs.randomElementPivot()
    averageRandomElementTime += qs.endTime()

    qs.initTime()
    qs.medianFirstMiddleLastElementPivot()
    averageMedianFirstMiddleLastElementTime += qs.endTime()
    
    # qs.initTime()
    # qs.medianThreeRandomElementPivot()
    # averageMedianThreeRandomElementTime += qs.endTime()


print("----------------------- Averages -----------------------")
print(f"First element pivot: {averageFirstElementTime}")
print(f"Middle element pivot: {averageMiddleElementTime}")
print(f"Last element pivot: {averageLastElementTime}")
print(f"Random element pivot: {averageRandomElementTime}")
print(f"Median first, middle, last element pivot: {averageMedianFirstMiddleLastElementTime}")
# print(f"Median three random element pivot: {averageMedianThreeRandomElementTime}")


print("----------------------- Single run -----------------------")
print(f"First element pivot: {firstElementTime}")
print(f"Middle element pivot: {middleElementTime}")
print(f"Last element pivot: {lastElementTime}")
print(f"Random element pivot: {randomElementTime}")
print(f"Median first, middle, last element pivot: {medianFirstMiddleLastElementTime}")
# print(f"Median three random element pivot: {medianThreeRandomElementTime}")


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

methods = ['FirstEl', 'MiddleEl', 'LastEl', 'RandomEl', 'MedianEl']
times = [firstElementTime, middleElementTime, lastElementTime, randomElementTime, medianFirstMiddleLastElementTime]
ax1.bar(methods, times)
ax1.set_ylabel('Time (s)')
ax1.set_xlabel('Pivot method')
ax1.set_title('Quick sort pivot method time comparison (Single run)')

averageTimes = [averageFirstElementTime, averageMiddleElementTime, averageLastElementTime, averageRandomElementTime, averageMedianFirstMiddleLastElementTime]
ax2.bar(methods, averageTimes)
ax2.set_ylabel('Time (s)')
ax2.set_xlabel('Pivot method')
ax2.set_title('Quick sort pivot method time comparison (Average)')

plt.tight_layout()

plt.savefig('basics-algorithms/sorting/results/quickSort.png')