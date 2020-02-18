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


def orderPizzas():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT

            # TODO: Write to output file
            # saveOutput(outputFile, outputDataFormatted)


def saveOutput(fileLocation, data):
    # TODO: Create output dir if not exists!
    with open(fileLocation, "w+") as f:
        f.write(data)


if __name__ == "__main__":
    orderPizzas()
