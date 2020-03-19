import random, pygame, sys

class sortingAlgorithms:

    def newarray(self, array, bars, max): # Makes a new array
        array.clear()
        for i in range(bars):
            array.insert(0, random.randint(1, max))


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
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]
            print(array)


    def cocktail(self, array): # Cocktail Sort
        a = len(array)
        print(array)
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]


            for k in range(a - i - 1, 0, -1):
                if array[k] < array[k-1]:
                    array[k], array[k-1] = array[k-1], array[k]
            print(array)


class bars:

    def __init__(self, height=0, width=10, windowWidth=800, windowHeight=600):
        self.height = height
        self.width = width
        self.x = windowWidth / 8
        self.y = windowHeight - height

        self.bar = pygame.Surface((self.width, self.height),
                                     pygame.SRCALPHA)
        self.bar.fill((255, 255, 255))

    def render(self, window):
        window.blit(self.bar, (self.x, self.y))
