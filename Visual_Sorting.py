class sortingAlgorithms:

    def select(self, array): # Select Sort
        array_sorted = []
        min = 0
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
        for i in range(len(array)):
            for k in range(len(array) - i - 1):
                pass


