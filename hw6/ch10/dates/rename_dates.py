#! python3
# renames filenames with american MM-DD-YYYY date format
# to european DD-MM-YYYY format

import shutil, os, re

date_pattern = re.compile(r'''^(.*?)  # all text before the date
    ((0|1)?\d)-        # one or two digits for the month
    ((0|1|2|3)?\d)-    # one or two digits for the day
    ((19|20)\d\d)      # four digits for the year
    (.*?)$             # all text after the date
    ''', re.VERBOSE)


# loop over files in working directory
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # skip files without a datels
    if mo == None:
        continue

    # get parts of filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # get full absolute file paths
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # rename files
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    shutil.move(amer_filename, euro_filename)