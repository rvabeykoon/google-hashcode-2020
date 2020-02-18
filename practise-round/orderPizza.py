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


def iterateFromLeft(arr, max):
    print("iterateFromLeft", arr, max)
    nElements = len(arr)

    highscore = 0
    highscoreSelection = []

    for leftTest in range(nElements):

        print("leftTest", leftTest)

        maxSumFromLeft, maxSumFromLeftSelect = iterateFromLeft(arr[0:leftTest], max - highscore)

        if maxSumFromLeft > highscore and maxSumFromLeft < max:
            highscore = maxSumFromLeft
            highscoreSelection = maxSumFromLeftSelect

        if maxSumFromLeft +

        # if maxSumFromLeft == 0:
        #     if highscore + arr[leftTest] < max:
        #         highscore += arr[leftTest]
        #         highscoreSelection += [leftTest]

    print("highscore", highscore, highscoreSelection)
    return highscore, highscoreSelection

iterateFromLeft([1, 2], 3)



# def fillFromLeft(arrPart, max):
#     nElements = len(arrPart)
#     print("DEBUG: fillFromLeft with {} elements, max {}".format(nElements, max))

#     best, bestSelect = 0, []

#     count, selection = 0, []
#     initCount, initSelect = 0, []

#     for rightStop in range(nElements, 0, -1):
#         print("Debug: RightStop: {}".format(rightStop))
#         if not rightStop == nElements:
#             initCount += arrPart[rightStop]
#             initSelect = initSelect + [arrPart[rightStop]]

#         count = initCount
#         selection = initSelect
#         for leftLookup in range(rightStop):
#             print("Looking at {}x{}".format(rightStop, leftLookup))

#             print("Solution for this iteration ({}): {}".format(count, selection))

# fillFromLeft([1, 2, 3, 4, 5], 10)



    #     count += arrPart[i]
    #     selection += [i]

    #     if count <= max and best < count:
    #         best = count
    #         bestSelect = selection

    # return best, bestSelect


# def calculateOrder(line1, line2):

#     # Start by extracting information from first line: "Control line"
#     itemsLine1 = line1.split(" ")
#     itemsLine2 = line2.split(" ")

#     maxSlices = int(itemsLine1[0])
#     pizzaCount = int(itemsLine1[1])

#     highestCount = -1
#     highestCountSolution = []

#     # Start from most right and work through to left for starting items
#     for startingIndexRight in range(pizzaCount, 0):
#         for fillingIndexLeft in range(pizzaCount)

#         tmpSelection = [i]
#         tmpSlices = int(itemsLine2[i])
#         analysisIndex = 0  # Start at selected (next) most left

#         while analysisIndex < pizzaCount and tmpSlices < maxSlices:
#             tmpSelection = tmpSelection + [analysisIndex]
#             tmpSlices += int(itemsLine2[analysisIndex])
#             analysisIndex += 1

#         if tmpSlices > highestCount and tmpSlices <= maxSlices:
#             print("New best with {} slices of pizzas: {}".format(tmpSlices, tmpSelection))
#             highestCount = tmpSlices
#             highestCountSolution = tmpSelection

#     return highestCount, highestCountSolution


def orderPizzas():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            pass
            # outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT

            # # We know that there are exactly two lines in each file.
            # outputCount, outputData = 12, 12 # calculateOrder(f.readline(), f.readline())

            # outputDataFormatted = str(outputCount) + "\n"
            # for i in outputData:
            #     outputDataFormatted += str(i) + " "

            # saveOutput(outputFile, outputDataFormatted)


def saveOutput(fileLocation, data):
    # TODO: Create output dir if not exists!
    with open(fileLocation, "w+") as f:
        f.write(data)


if __name__ == "__main__":
    orderPizzas()
