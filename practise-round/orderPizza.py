#!/bin/python3

# TODO: Write unit tests

SEP = "/"
INPUT_DATA_FOLDER = "input-data-sets"
INPUT_DATA_FILES = [
    "a_example",
    "b_small",
    "c_medium",
    "d_quite_big",
    "e_also_big"
]
INPUT_DATA_EXT = ".in"
OUTPUT_DATA_DIR = "out"
OUTPUT_DATA_EXT = ".out"


def orderPizzas():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT

            # print(f.readlines())
            getBestPizzaOrder(inputLines = f.readlines())
            outputData = ""

            saveOutput(outputFile, outputData)


def getBestPizzaOrder(inputLines):
    firstLine = True
    maxSlices = 0               # maximum slices to order
    difPizzas = 0               # number of different pizzas available == len(numberOfSlicesPerPizza)
    numberOfSlicesPerPizza = [] # list with the number of slices per pizza

    for line in inputLines:
        line = line.strip('\n')
        numberList = line.split(' ')
        if(firstLine):
           maxSlices = int(numberList[0])
           difPizzas = int(numberList[1])
           firstLine = False
        else:
            numberOfSlicesPerPizza = numberList

    sortFromLeftToRight(maximumSlices=maxSlices, differentPizzas=difPizzas, slicesPerPizza=numberOfSlicesPerPizza)

    return


def sortFromLeftToRight(maximumSlices: int, differentPizzas: int, slicesPerPizza: list):
    maximumSliceSum = 0
    pizzaSelection = differentPizzas * '0'

    i = -1
    currentSliceSum = 0
    lastSliceNumberAdded = 0

    for sliceNumber in slicesPerPizza:
        sliceNumber = int(sliceNumber)
        i += 1

        if(currentSliceSum < maximumSlices):
            lastSliceNumberAdded = sliceNumber
            currentSliceSum += sliceNumber
            pizzaSelection = pizzaSelection[:i] + '1' + pizzaSelection[i + 1:] # replace the 0 in the selectionString with a 1

        else:
            print(pizzaSelection)
            maximumSliceSum = currentSliceSum - lastSliceNumberAdded
            print(maximumSliceSum)
            return

        #print(sliceNumber)

    print(pizzaSelection)
    
    return


def saveOutput(fileLocation, data):
    # TODO: Create output dir if not exists!
    with open(fileLocation, "w+") as f:
        f.write(data)


if __name__ == "__main__":
    orderPizzas()
