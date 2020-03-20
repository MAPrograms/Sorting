from Visual_Sorting import *

# Pygame variables
windowWidth = 1366
windowHeight = 768
# Pygame stuff
pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight))

FPS = 15
clock = pygame.time.Clock()

# Sorting Stuff
array = [20, 30, 40, 50, 10]
sorting = sortingAlgorithms()

# Bar stuff
bar_list = []
sorting.newarray(array, 120, 400)
#print(array)
c = 0
for i in array:
    bar = bars(height=i, spacing=5, width=5, a=len(array), windowWidth=windowWidth, windowHeight=windowHeight)
    bar_list.append(bar)
    bar_list[c].x = bar_list[c - 1].x + bar_list[c].width + bar_list[c].spacing
    c += 1

#sorting.select(array)

#sorting.bubble(array)

#sorting.cocktail(array)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((56, 56, 56))

    sorting.bubble(array)
    # for l in range(len(array)):
    #     if array[l] != bar_list[l].height:
    #         bar_list.clear()
    #         c = 0
    #         for i in array:
    #             bar = bars(height=i, spacing=5, width=5, a=len(array), windowWidth=windowWidth, windowHeight=windowHeight)
    #             bar_list.append(bar)
    #             bar_list[c].x = bar_list[c - 1].x + bar_list[c].width + bar_list[c].spacing
    #             c += 1
    for l in range(len(array)):
        if array[l] != bar_list[l].height:
            bar_list[l].x, bar_list[l].x = bar_list[l].x, bar_list[l].x

    for j in range(len(bar_list)):
        bar_list[j].render(window)

    pygame.display.update()
    clock.tick(FPS)
