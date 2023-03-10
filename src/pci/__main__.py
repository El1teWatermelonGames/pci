from os import name, system, path, remove
from keyboard import read_key
from time import sleep

system("") # init terminal

# Uses hexadecimal color system (16 colors to pick from)

# 0 | BLACK
# 1 | RED
# 2 | GREEN
# 3 | YELLOW
# 4 | BLUE
# 5 | MAGENTA
# 6 | CYAN
# 7 | WHITE
# 8 | BRIGHT BLACK
# 9 | BRIGHT RED
# A | BRIGHT GREEN
# B | BRIGHT YELLOW
# C | BRIGHT BLUE
# D | BRIGHT MAGENTA
# E | BRIGHT CYAN
# F | BRIGHT WHITE

# ----- Data -----
debug = False

keySens = 0.1

CEND = "\u001b[0m"

CBLACK = "\u001b[40m"
CRED = "\u001b[41m"
CGREEN = "\u001b[42m" 
CYELLOW = "\u001b[43m"
CBLUE = "\u001b[44m"
CMAGENTA = "\u001b[45m"
CCYAN = "\u001b[46m"
CWHITE = "\u001b[47m"
CBBLACK = "\u001b[40;1m"
CBRED = "\u001b[41;1m"
CBGREEN = "\u001b[42;1m"
CBYELLOW = "\u001b[43;1m"
CBBLUE = "\u001b[44;1m"
CBMAGENTA = "\u001b[45;1m"
CBCYAN = "\u001b[46;1m"
CBWHITE = "\u001b[47;1m"

splashScreen = [
    "FFF000FFF00FFF",
    "F0F00F000000F0",
    "FFF00F000000F0",
    "F0000F000000F0",
    "F00000FFF00FFF"
]

editorHeaderColors = [
    "0123456789ABCDEF"
]

editorHeaderSpacing = [
    "FFFFFFFFFFFFFFFFFFFFFF"
]

editorHeaderControls = "q = Quit  |  s = Save  |  n = New Line  |  k = Backspace  |  m = Revert Save"

allowedKeys = [ 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F' ]

# ----- Process -----

def clearConsole():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def processLines(image):
    image = open(image, 'r') # Open the image file
    data = []
    for line in image:
        data.append(line.replace("\n", "")) # Remove \n character from start of line and add the line to the list
    image.close()
    return data

def processPixel(data, patfile):
    out = []
    for line in data: # Cycle through each line of data
        newLine = ""
        for char in line: # Cycle through character
            if patfile == False: char = char.replace(char, appendPixel(char, "  ")) # Normal image processing
            if patfile == True: char = char.replace(char, appendPixel(char, char+" ")) # Pat file processing
            newLine += char
        out.append(newLine)
    return out

def appendPixel(char, outChar):
    out = ""
    if char == "0": out = CBLACK
    elif char == "1": out = CRED
    elif char == "2": out = CGREEN
    elif char == "3": out = CYELLOW
    elif char == "4": out = CBLUE
    elif char == "5": out = CMAGENTA
    elif char == "6": out = CCYAN
    elif char == "7": out = CWHITE
    elif char == "8": out = CBBLACK
    elif char == "9": out = CBRED
    elif char == "A": out = CBGREEN
    elif char == "B": out = CBYELLOW
    elif char == "C": out = CBBLUE
    elif char == "D": out = CBMAGENTA
    elif char == "E": out = CBCYAN
    elif char == "F": out = CBWHITE
    elif char == " ": out = CEND
    else:
        print(f"Invalid char in image file: {char}")
        exit(1)
    return str(out + outChar + CEND)


# ----- Front-end -----

def debugOut(text):
    if(debug): print(text)

def printImage(imageData):
    for line in imageData:
        print(line)

def printToolbar(Colors, Spacing):
    all = Colors + Spacing
    print("".join(all))

def renderer():
    while(True):
        # Get the file name/path and ensure it is valid
        fp = str(input("Enter the name of the image: "))
        patfile = False
        size = len(fp)

        if fp.endswith(" -pat"):
            patfile = True
            fp = fp[:size - 5]

        # Ensure it is a valid file format and account if the image is patted
        if fp.endswith(".pci"):
            # Process the data to an image
            out = processLines(fp) # Fetch the data and format into a list
            out = processPixel(out, patfile) # Convert each value into the color needed

            # Output each section of the array on individual lines
            clearConsole()
            printImage(out)
            input("\nPress enter to close window...")
            break
        else:
            clearConsole()
            print("Not a valid file format! Please use a Pixel Console Image file (.pci)")

def liveEditor(file):
    # --- Var Declaration ---
    output = []
    selectedRow = 0
    baseHeader = f"Pixel Console Editor | Editing: {file}"
    headerColor = CBWHITE
    extraHeader = f"                                    "

    # --- Live ---
    while(True):
        clearConsole()

        print(f"{headerColor}{baseHeader}{extraHeader}{CEND}")
        headerColor = CBWHITE
        extraHeader = f"                                    "

        print(CBWHITE + editorHeaderControls + CEND)
        printToolbar(
            processPixel(editorHeaderColors, True),
            processPixel(editorHeaderSpacing, False)
        )
        print("\n")
        # Render current state of the image
        printImage(processPixel(output, True))

        # Allow input of next character & clear console
        key = str(read_key())
        sleep(keySens)
        print()

        # Process input
        if key == 'q':
            clearConsole()
            exit(0)
        elif key == 's':
            remove(file)
            f = open(file, "a")
            f.write("\n".join(output))
            f.close()
            remove(file + ".pce")
            f = open(file + ".pce", "a")
            f.write(str(selectedRow))
            f.close()

            headerColor = CBGREEN
            extraHeader = " | Saved                            "
        elif key == 'n':
            selectedRow += 1
        elif key == 'm':
            output = processLines(file)
            f = open(file + ".pce", "r")
            selectedRow = int(f.read()[0])
            f.close()

            headerColor = CBRED
            extraHeader = " | Reverted to last save            "
        elif key == 'k':
            if(len(output[selectedRow]) > 0):
                output[selectedRow] = output[selectedRow].rstrip(output[selectedRow][-1])
        elif key.isdigit() or key.isalpha() and key in allowedKeys:
            if len(output) - 1 == selectedRow:
                output[selectedRow] += key.upper()
            else:
                output.append(key.upper())
        

def editor():
    filename = input("Name the new file (do not include the file extension): ") + ".pci"
    exists = path.exists(filename)

    if(exists):
        while(True):
            selection = input("A file with this name already exists, are you sure you want to continue (y/n): ")
            if selection == "y":
                remove(filename)
                file = open(filename, "x")
                file.close()
                file = open(filename + ".pce", "a")
                file.write(str(0))
                file.close()
                break
            elif selection == "n":
                exit(0)
    else:
        file = open(filename, "x")
        file.close()
        file = open(filename + ".pce", "a")
        file.write(str(0))
        file.close()

    liveEditor(filename)

def main():
    printImage(processPixel(splashScreen, False))

    while(True):
        key = str(input("1. Renderer\n2. Editor\n"))[0]
        if key == "1":
            renderer()
            break
        elif key == "2":
            editor()
        elif key == "d":
            if debug: debug = False
            else: debug = True
        clearConsole()