import math
import timeit
import numpy
import random
from Sort import Sort
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

sort1 = Sort()
mergeSortTimes = []
insertionSortTimes = []


def howManyRandomNumber(x):
    f = open("keys" + str(x) + ".txt", "w")
    for y in range(0, x):
        array[y] = random.randint(0, 100000)
        f.write(str(array[y]) + "\n")
    f.close()


def saveMergeSortedList(x):
    f = open("mergeSortedKeys" + str(x) + ".txt", "w")
    for y in range(0, x):
        f.write(str(array[y]))
        f.write("\n")
    f.close()


def saveInsertionSortedList(x):
    f = open("InsertionSortedKeys" + str(x) + ".txt", "w")
    for y in range(0, x):
        f.write(str(array1[y]))
        f.write("\n")
    f.close()


def saveCompletionTimes():
    f = open("InsertionSortTimes.txt", "w")
    for i in range(0, 5):
        f.write(str(insertionSortTimes[i]))
        f.write("\n")
    f.close()
    f = open("MergeSortTimes.txt", "w")
    for i in range(0, 5):
        f.write(str(mergeSortTimes[i]))
        f.write("\n")
    f.close()


def loadRandomKeys(x):
    f = open("keys" + str(x) + ".txt", "r")
    for i in range(0, x):
        array1[i] = int(f.readline())
    f.close()


for x in range(1, 6):
    array = numpy.empty(int(math.pow(10, x)), dtype=int)
    howManyRandomNumber(int(math.pow(10, x)))
    startTime = timeit.default_timer()
    sort1.mergeSort(array, 1, int(len(array)))
    mergeSortTimes.append(timeit.default_timer() - startTime)
    saveMergeSortedList(int(math.pow(10, x)))

for x in range(1, 6):
    array1 = numpy.empty(int(math.pow(10, x)), dtype=int)
    loadRandomKeys(int(math.pow(10, x)))
    startTime = timeit.default_timer()
    sort1.insertionSort(array1, int(len(array1)))
    insertionSortTimes.append(timeit.default_timer() - startTime)
    saveInsertionSortedList(int(math.pow(10, x)))

saveCompletionTimes()
keys = numpy.array([10, 100, 1000, 10000, 100000])
model1 = make_interp_spline(keys, mergeSortTimes)
model2 = make_interp_spline(keys, insertionSortTimes)

xs1 = numpy.linspace(100000, 3)
ys1 = model1(xs1)
xs2 = numpy.linspace(100000, 28)
ys2 = model2(xs2)

plt.ylim([0, 3])
plt.title('MergeSort Times')
plt.plot(xs1, ys1)
plt.ylabel('Sort Complete Times')
plt.xlabel('Number of Keys')
plt.xscale("log")
plt.show()

plt.ylim([0, 28])

plt.title('InsertionSort Times')
plt.plot(xs2, ys2)
plt.ylabel('Sort Complete Times')
plt.xlabel('Number of Keys')
plt.xscale("log")
plt.show()
