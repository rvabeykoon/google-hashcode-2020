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
            print(fileBase + ' calculating...')
            outputData = getBestPizzaOrder(inputLines = f.readlines())

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

    numberOfPizzas, typesOfPizzas = sortFromLeftToRight(maximumSlices=maxSlices, differentPizzas=difPizzas, slicesPerPizza=numberOfSlicesPerPizza)

    outputLines = '' + str(numberOfPizzas) + '\n' + ' '.join(typesOfPizzas)

    return outputLines


def sortFromLeftToRight(maximumSlices: int, differentPizzas: int, slicesPerPizza: list):
    maximumSliceSum = 0
    maximumSelection = ''
    
    for outer_index in range (differentPizzas):
        pizzaSelection = differentPizzas * '0'
        currentSliceSum = 0

        for index in range(differentPizzas):
            numberToSelect = (index + outer_index) % differentPizzas
            sliceNumber = int(slicesPerPizza[numberToSelect])

            if(currentSliceSum + sliceNumber <= maximumSlices):
                currentSliceSum += sliceNumber
                pizzaSelection = pizzaSelection[:numberToSelect] + '1' + pizzaSelection[numberToSelect + 1:] # replace the 0 in the selectionString with a 1

            else:
                if currentSliceSum > maximumSliceSum:
                    maximumSliceSum = currentSliceSum
                    maximumSelection = pizzaSelection

        if(maximumSliceSum == maximumSlices):
            break # stop the calculation early, if maximum slices is already EXACTLY reached!

    print('Number of slices ordered: ' + str(maximumSliceSum))
    numberOfPizzasToOrder, typesOfPizzas = getOutputInformation(selection=maximumSelection)

    return numberOfPizzasToOrder, typesOfPizzas


def getOutputInformation(selection: str):
    typesOfPizzas = []

    index = -1
    for character in selection:
        index += 1

        if character == '1':
            typesOfPizzas.append(str(index))

    return len(typesOfPizzas), typesOfPizzas


def saveOutput(fileLocation, data):
    # TODO: Create output dir if not exists!
    with open(fileLocation, "w+") as f:
        f.write(data)


if __name__ == "__main__":
    orderPizzas()
