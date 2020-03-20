import random, pygame, sys

class sortingAlgorithms:

    def newarray(self, array, bars, max): # Makes a new array
        array.clear()
        for i in range(bars):
            array.insert(0, random.randint(5, max))


    def selection(self, array): # Select Sort
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
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]
            break




    def cocktail(self, array): # Cocktail Sort
        a = len(array)
        for i in range(a):
            for k in range(a - i - 1):
                if array[k] > array[k+1]:
                    array[k], array[k+1] = array[k+1], array[k]

            for k in range(a - i - 1, 0, -1):
                if array[k] < array[k-1]:
                    array[k], array[k-1] = array[k-1], array[k]
            break


class bars:

    def __init__(self, height=0, width=10, spacing=10, windowWidth=800, windowHeight=600, a=0):
        self.height = height
        self.spacing = spacing
        self.width = width
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.a = a
        self.x = windowWidth / 2 - self. width / 2 - ((a + 1) * (width / 2 + self.spacing / 2))
        self.y = windowHeight - height

        self.bar = pygame.Surface((self.width, self.height))
        self.bar.fill((0, 162, 232))

    def render(self, window):
        window.blit(self.bar, (self.x, self.y))
