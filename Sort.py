import numpy
import dcst


class Sort:
    def insertionSort(self, array, length):
        for j in range(1, length):
            key = array[j]
            i = j - 1
            while i >= 0 and array[i] > key:
                array[i + 1] = array[i]
                i = i - 1
                array[i + 1] = key

    def mergeSort(self, array, front, rear):
        if int(front) < int(rear):
            middle = int((front + rear) / 2)
            self.mergeSort(array, front, middle)
            self.mergeSort(array, middle + 1, rear)
            self.merge(array, front, middle, rear)

    def merge(self, array, front, middle, rear):
        leftLength = int(middle - front + 1)
        rightLength = int(rear - middle)

        left = numpy.array(range(leftLength + 1))
        right = numpy.array(range(rightLength + 1))

        for i in range(0, leftLength):
            left[i] = array[front + i - 1]
        for j in range(0, rightLength):
            right[j] = array[middle + j]
        left[leftLength] = 100000
        right[rightLength] = 100000
        i = 0
        j = 0

        front = front - 1
        for k in range(front, rear):
            if left[i] <= right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
