#!/bin/python3

SEP = "/"
INPUT_DATA_FOLDER = "library-in-files"
INPUT_DATA_FILES = [
    "a_example",
    #"b_read_on",
    #"c_incunabula",
    #"d_tough_choices",
    #"e_so_many_books",
    #"f_libraries_of_the_world"
]
INPUT_DATA_EXT = ".txt"
OUTPUT_DATA_DIR = "out"
OUTPUT_DATA_EXT = ".out"

def scanBooks():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT



if __name__ == "__main__":
    scanBooks()
