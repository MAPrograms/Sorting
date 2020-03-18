
class sortingAlgorithms:

    def selectsort(self):
        array = [4, 2, 5, 7, 1, 3]
        array_sorted = []
        sort = True
        min = 0
        while sort:
            for numbers in array:
                if numbers > min:
                    min = numbers
            if min != 0:
                array_sorted.insert(0, min)

            if len(array) != 1:
                array.remove(min)
                print(array_sorted)
            else:
                sort = False
            min = 0

        print(array_sorted)

sortingAlgorithms.selectsort()
