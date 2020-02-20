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


def importProblemStatement():
    for fileBase in INPUT_DATA_FILES:
        with open(INPUT_DATA_FOLDER + SEP + fileBase + INPUT_DATA_EXT, "r") as f:
            outputFile = OUTPUT_DATA_DIR + SEP + fileBase + OUTPUT_DATA_EXT

            meta, libraries = parseProblemStatement(f)

            print('Parsed problem statement ({}):\n'.format(fileBase), meta, '\n', libraries)

            signupLibsAndScanBooks(meta, libraries)


def signupLibsAndScanBooks(meta, libraries):

    # Best library (highest throughput)
    # rank all libs order by highest <value>
    registeredLibs = []
    inLibraryRegisteringProcess = False

    # POroceed through days
    for day in days:
        if not inLibraryRegisteringProcess:
            registeredLibs += <lib>
            <lib>['signupStarted'] = day
            inLibraryRegisteringProcess = True
        if libDoneRegistering(registeredLibs[-1]):
            inLibraryRegisteringProcess = False

        for libsDoneRegistering(registeredLibs, day):
            # order book by value in bookIds
            # scan highest
            # sort out already scanned --> library['booksScanned'] = []

    return registeredLibs  # abzüglich die die noch nicht fertig regoistriert sind!!!!


def libsDoneRegistering(registeredLibs, currentDay):
    # Filter out not done registering

    # registeredLib in registeredLibs
    # if <lib>['signupStarted'] + day <= signupDays
    pass

    # Register libs
    # Scan books (order by highest) for already registered libs

    return OUTPUTDATA


def parseProblemStatement(problemFile):
    line1 = problemFile.readline().replace('\n', '')
    numberOfBooks, numberOfLibs, days = line1.split(' ')

    line2 = problemFile.readline().replace('\n', '')
    bookScores = line2.split(' ')

    meta = {'days': days, 'bookScores': bookScores}

    libraries = []

    for lib in range(int(numberOfLibs)):
        library = {'id': lib}
        libLine1 = problemFile.readline().replace('\n', '').split(' ')
        libLine2 = problemFile.readline().replace('\n', '').split(' ')

        library['booksCount'] = libLine1[0]
        library['signupDays'] = libLine1[1]
        library['booksShippingPerDay'] = libLine1[2]
        library['bookIds'] = libLine2

        library['booksScanned'] = []

        libraries += [library]

    return meta, libraries


if __name__ == "__main__":
    importProblemStatement()
