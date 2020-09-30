#! python3
'''
adds bullet points to the start of each new line

step 1: copy text
step 2: run python3 bullet-point-adder.py
step 3: paste text

output should look like:

* list of animals
* list of aquariam life
* list of cultivars
'''

import pyperclip 

text = pyperclip.paste()

# separate lines and add stars
lines = text.split('\n')

# loop through each line and add star to beginning of line
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)