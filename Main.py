from Visual_Sorting import *

done = False
# Pygame variables
windowWidth = 800
windowHeight = 600
# Pygame stuff
pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight))

# Sorting Stuff
array = [20, 30, 40, 50, 10]
sorting = sortingAlgorithms()

# Bar stuff
bar_list = []

#sorting.newarray(array, 25, 100)

#sorting.select(array)

#sorting.bubble(array)

#sorting.cocktail(array)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0, 0, 0))

    if len(bar_list) != len(array):
        for i in array:
            bar = bars(height=i)
            bar_list.append(bar)
        done = True

    for j in range(len(bar_list)):
        if done == True:
            bar_list[j].x += bar_list[j-1].x - 80
        bar_list[j].render(window)

    done = False

    pygame.display.update()

