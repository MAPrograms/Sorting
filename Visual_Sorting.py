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
white = (255, 255, 255)

# Variables for the top bar
topbarX = 0
topbarY = 0
topbarHeight = 70

# Variables for underline bar
underlinebarX = 0
underlinebarY = 70
underlinebarHeight = 3


# Variables for the buttons
btnWidth = 70
btnHeight = 20
pygame.font.init()
pygame.font.get_fonts()
# ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'extra', 'fzshuti', 'fzyaoti', 'lisu', 'stcaiyun', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'youyuan', 'haettenschweiler', 'msoutlook', 'bookantiqua', 'centurygothic', 'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'garamond', 'monotypecorsiva', 'bookmanoldstyle', 'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'berlinsansfbdemi', 'bernardcondensed', 'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb', 'centaur', 'chiller', 'colonna', 'cooperblack', 'footlight', 'freestylescript', 'harlowsolid', 'harrington', 'hightowertext', 'jokerman', 'juiceitc', 'kristenitc', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'magneto', 'maturascriptcapitals', 'mistral', 'modernno20', 'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment', 'playbill', 'poorrichard', 'ravie', 'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin', 'century', 'wingdings2', 'wingdings3', 'arialms', 'msmincho', 'acaderef', 'aigdt', 'amdtsymbols', 'geniso', 'amgdt', 'bankgothic', 'bankgothicmedium', 'cityblueprint', 'commercialpi', 'commercialscript', 'countryblueprint', 'dutch801roman', 'dutch801', 'dutch801extra', 'euroroman', 'euroromanoblique', 'monospace821', 'panroman', 'romantic', 'romans', 'sansserif', 'sansserifboldoblique', 'sansserifoblique', 'stylus', 'superfrench', 'swiss721', 'swiss721outline', 'swiss721condensed', 'swiss721condensedoutline', 'swiss721blackcondensed', 'swiss721extended', 'swiss721blackextended', 'swiss721black', 'swiss721blackoutline', 'technicbold', 'techniclite', 'technic', 'universalmath1', 'vineta', 'isocpeur', 'isocteur', 'proxy9', 'proxy8', 'proxy7', 'proxy6', 'proxy5', 'proxy4', 'proxy3', 'symusic', 'symeteo', 'symath', 'symap', 'syastro', 'romant', 'romand', 'romanc', 'italict', 'greeks', 'greekc', 'gothicg', 'gothice', 'txt', 'simplex', 'scripts', 'scriptc', 'proxy2', 'proxy1', 'monotxt', 'italicc', '', 'isoct3', 'isoct2', 'isoct', 'isocp3', 'isocp2', 'isocp', 'gothici', 'gdt', 'complex', 'thcadsymbsttf', 'thcadsymbs', 'zwadobef', 'eurosign', 'lucidabrightregular', 'lucidasansregular', 'lucidasanstypewriter', 'lucidasanstypewriterregular', 'adobeheitistdregular', 'adobemingstdlight', 'adobemyungjostdmedium', 'adobepistd', 'adobesongstdlight', 'courierstd', 'courierstdbold', 'courierstdboldoblique', 'courierstdoblique', 'kozgopr6nmedium', 'kozminpr6nregular', 'myriadcad', 'hyswlongfangsong', 'swastro', 'olfsimplesansocregular', 'swcomp', 'swgothe', 'swgothg', 'swgothi', 'swgrekc', 'swgreks', 'swisop1', 'swisop2', 'swisop3', 'swisot1', 'swisot2', 'swisot3', 'swital', 'switalc', 'switalt', 'swmap', 'swmath', 'swmeteo', 'swmono', 'swmusic', 'swromnc', 'swromnd', 'swromns', 'swromnt', 'swscrpc', 'swscrps', 'swsimp', 'swtxt', 'swgdt', 'swlink', 'dejavusansmono', 'dejavusansmonooblique', 'freesans']
font = pygame.font.SysFont('calibri', 12)

# Variables for the sort array btn
sortarraybtnX = 15
sortarraybtnY = 25

# Variables for new array btn
newarraybtnX = 100
newarraybtnY = 25

# Variables for the slider
sliderX = 620
sliderY = 35
sliderwidth = 136
sliderheight = 8

# Variables for btn on slider
sliderbtnX = 620
sliderbtnY = 31
sliderbtnwidth = 6
sliderbtnheight = 16
start = 10

# Variables for text above slider
slidertextX = 620
slidertextY = 15
arraysizetext = 'Array size: '

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

    def __init__(self, color, btn, text):
        self.color = color
        self.btnX = btn[0]
        self.btny = btn[1]
        self.width = btn[2]
        self.height = btn[3]
        self.text = text

    def render(self, window):
        pygame.draw.rect(window, self.color, (self.btnX, self.btny, self.width, self.height))
        text = font.render(self.text, True, white)
        window.blit(text, (self.btnX + (self.width / 2) - (text.get_width() / 2), self.btny + (self.height / 2) - (text.get_height() / 2)))

def arraySizeFromSlider(sliderbtnX, start):
    newArraySize = sliderbtnX - 620 + start
    return newArraySize