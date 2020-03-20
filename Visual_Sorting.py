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
btnWidth = 70
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 12)

# Variables for the sort array btn
sortarraybtnX = 15
sortarraybtnY = 25

# Variables for new array btn
newarraybtnX = 100
newarraybtnY = 25

# Create rectangles
class rectangle:

    def __init__(self, color, rect):
        self.color = color
        self.rectX = rect[0]
        self.recty = rect[1]
        self.width = rect[2]
        self.height = rect[3]

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.rectX, self.recty, self.width, self.height))

# Create Buttons
class btn:

    def __init__(self, color, btn):
        self.color = color
        self.btnX = btn[0]
        self.btny = btn[1]
        self.width = btn[2]
        self.height = btn[3]
        self.text = btn[4]

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.btnX, self.btny, self.width, self.height))
        text = font.render(self.text, True, (255, 255, 255))
        window.blit(text, (self.btnX + (self.width / 2) - (text.get_width() / 2), self.btny + (self.height / 2) - (text.get_height() / 2)))