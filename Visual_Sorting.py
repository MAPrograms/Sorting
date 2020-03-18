import random

class sortingAlgorithms:

    def newarray(self, array, x): # Makes a new array
        array.clear()
        for i in range(x):
            array.insert(0, random.randint(1, 9))


    def select(self, array): # Select Sort
        array_sorted = []
        min = 0
        print(array)
        for i in range(len(array)):
            for numbers in array:
                if numbers > min:
                    min = numbers
            if min != 0:
                array_sorted.insert(0, min)

            array.remove(min)
            print(array_sorted)
            min = 0


    def bubble(self, array): # Bubble Sort
        a = len(array)
        print(array)
        count = 0
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]
                    print(array)
                    count += 1
        print(count)


    def cocktail(self, array): # Cocktail Sort
        a = len(array)
        print(array)
        count = 0
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]
                    print(array)
                    count += 1

            for k in range(a - i - 1, 0, -1):
                if array[k] < array[k-1]:
                    array[k], array[k-1] = array[k-1], array[k]
                    print(array)
                    count += 1
        print(count)



