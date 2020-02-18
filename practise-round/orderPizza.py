#!/bin/python3

# TODO: Write unit tests

SEP = "/"
INPUT_DATA_FOLDER = "input-data-sets"
INPUT_DATA_FILES = [
    "a_example",
    #"b_small",
    #"c_medium",
    #"d_quite_big",
    #"e_also_big"
]
INPUT_DATA_EXT = ".in"
OUTPUT_DATA_DIR = "out"
OUTPUT_DATA_EXT = ".out"


def calculateOrder(line1, line2):

    # Start by extracting information from first line: "Control line"
    itemsLine1 = line1.split(" ")
    itemsLine2 = line2.split(" ")

    maxSlices = int(itemsLine1[0])
    pizzaCount = int(itemsLine1[1])

    highestCount = -1
    highestCountSolution = []

    # Start from most left and work through to right for starting items
    for i in range(pizzaCount):
        tmpSelection = [i]
        tmpSlices = int(itemsLine2[i])
        analysisIndex = i  # Start at selected (next) most left

        while analysisIndex < pizzaCount-1 and tmpSlices < maxSlices:
            analysisIndex += 1
            tmpSelection += [analysisIndex]
            tmpSlices += int(itemsLine2[analysisIndex])
        if tmpSlices > highestCount and tmpSlices <= maxSlices:
            print("New best with {} slices of pizzas: {}".format(tmpSlices, tmpSelection))
            highestCount = tmpSlices
            highestCountSolution = tmpSelection

    return highestCount, highestCountSolution


def orderPizzas():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT

            # We know that there are exactly two lines in each file.
            outputCount, outputData = calculateOrder(f.readline(), f.readline())

            outputDataFormatted = str(outputCount) + "\n"
            for i in outputData:
                outputDataFormatted += str(i) + " "

            saveOutput(outputFile, outputDataFormatted)


def saveOutput(fileLocation, data):
    # TODO: Create output dir if not exists!
    with open(fileLocation, "w+") as f:
        f.write(data)


if __name__ == "__main__":
    orderPizzas()
