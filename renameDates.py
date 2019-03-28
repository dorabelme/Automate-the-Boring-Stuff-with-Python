# It searches all the filenames in the current working directory for American-style dates
# When one is found, it renames the file with the month and day swapped to make it European-stype

# Create a regex that can identify the text pattern of American-stype dates
# Call os.listdir( ) to find all the files in the working directory
# Loop over each filename, using the regex to check whether it has a date
# If it has a date, rename the file with shutil.move( )

#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches files with the American date format
datePattern = re.compile(r"""(.*?)          # all text before the date
        ((0|1)?\d)-                         # one or two digits for the month
        ((0|1|2|3)?\d)-                     # one or two digits for the day
        ((19|20)\d\d)                       # four digits for the year
        (.*?)$                              # all text after the date
        """, re.VERBOSE)

# datePattern = re.compile(r"""(1)           # all text before the date
#        (2 (3) )-                           # one or two digits for the month
#        (4 (5) )-                           # one or two digits for the day
#        (6 (7) )                            # four digits for the year
#        (8)$                                # all text after the date
#        """, re.VERBOSE)

# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # TODO: Skip files without a date.
    if mo == None:
        continue

    # TODO: Get the different parts of the filename.

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo. group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: Form the European-stype filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: Rename the files
    print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))

    # shutil.move(amerFilename, euroFilename)
    # uncomment after testing

