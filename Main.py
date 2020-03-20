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

# Mouse event stuff
mousebtnup = False

#sorting.select(array)

#sorting.bubble(array)

#sorting.cocktail(array)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((56, 56, 56))

    # Creates the top bar
    topbar = rectangle(grey, (topbarX, topbarY, windowWidth, topbarHeight))
    topbar.render(window)

    # Creates the underline bar
    underlinebar = rectangle(blue, (underlinebarX, underlinebarY, windowWidth, underlinebarHeight))
    underlinebar.render(window)

    # Creates the different buttons
    sortarraybtn = btn(blue, (sortarraybtnX, sortarraybtnY, btnWidth, btnHeight, "Sort Array"))
    sortarraybtn.render(window)

    newarraybtn = btn(blue, (newarraybtnX, newarraybtnY, btnWidth, btnHeight, "New Array"))
    newarraybtn.render(window)

    # To make sure it only runs once per mouse click
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousebtnup = True

    # Event for clicking on New Array button
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and mousebtnup:
            if event.pos[0] >= newarraybtnX and event.pos[0] <= newarraybtnX + newarraybtn.width:
                if event.pos[1] >= newarraybtnY and event.pos[1] <= newarraybtnY + newarraybtn.height:
                    sorting.newarray(array, 10, 100)
                    print("Done making a new Array")
                    mousebtnup = False

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and mousebtnup:
            if event.pos[0] >= sortarraybtnX and event.pos[0] <= sortarraybtnX + sortarraybtn.width:
                if event.pos[1] >= sortarraybtnY and event.pos[1] <= sortarraybtnY + sortarraybtn.height:
                    sorting.selection(array)
                    mousebtnup = False

    sorting.bubble(array)
     #for l in range(len(array)):
     #    if array[l] != bar_list[l].height:
     #        bar_list.clear()
     #        c = 0
     #        for i in array:
     #            bar = bars(height=i, spacing=5, width=5, a=len(array), windowWidth=windowWidth, windowHeight=windowHeight)
     #            bar_list.append(bar)
     #            bar_list[c].x = bar_list[c - 1].x + bar_list[c].width + bar_list[c].spacing
     #            c += 1
    for l in range(len(array)):
        if array[l] != bar_list[l].height:
            bar_list[l].x, bar_list[l].x = bar_list[l].x, bar_list[l].x

    for j in range(len(bar_list)):
        bar_list[j].render(window)

    pygame.display.update()
    clock.tick(FPS)
