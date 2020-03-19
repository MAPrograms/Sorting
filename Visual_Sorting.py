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

        self.bar = pygame.Surface((self.width, self.height))
        self.bar.fill((255, 255, 255))

    def render(self, window):
        window.blit(self.bar, (self.x, self.y))


# Variables for color
grey = (98, 98, 98)
blue = (0, 162, 232)

# Variables for the top bar
topbarX = 0
topbarY = 0
topbarHeight = 70

# Variables for underline bar
underlinebarX = 0
underlinebarY = 70
underlinebarHeight = 3


# Variables for the buttons
btnHeight = 20
btnWidth = 65

# Variables for the sort array btn
sortarraybtnX = 15
sortarraybtnY = 25

# Variables for new array btn
newarraybtnX = 100
newarraybtnY = 25

# Create rectangles and renders them
class rectangle:
    def __init__(self, color, rect):
        self.color = color
        self.rectX = rect[0]
        self.recty = rect[1]
        self.width = rect[2]
        self.height = rect[3]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.rectX, self.recty, self.width, self.height))