# Homework 2: Chapter 10: Grep and Regex

## egrep

**egrep** will search a given set of data and print every line which contains a given pattern

`egrep [command line options] <pattern> [path]`

egrep will print the entire line for every line which contains a string of characters matching the given pattern

    user@bash: egrep 'mellon' mysampledata.txt
    Mark watermellons 12
    Oliver rockmellons 2


prints number lines associated with matches

    user@bash: egrep -n 'mellon' mysampledata.txt
    3:Mark watermellons 12
    11:Oliver rockmellons 2

shows the number of lines that matched the pattern

    user@bash: egrep -c 'mellon' mysampledata.txt
    2

## Regular expression overview

- `.` (dot) - a single character.
- `?` - the preceding character matches 0 or 1 times only.
- `*` - the preceding character matches 0 or more times.
- `+` - the preceding character matches 1 or more times.
- `{n}` - the preceding character matches exactly n times.
- `{n,m}` - the preceding character matches at least n times and not more than m times.
- `[agd]` - the character is one of those included within the square brackets.
- `[^agd]` - the character is not one of those included within the square brackets.
- `[c-f]` - the dash within the square brackets operates as a range. In this case it means either the letters c, d, e or f.
- `()` - allows us to group several characters to behave as one.
- `|` (pipe symbol) - the logical OR operation.
- `^` - matches the beginning of the line.
- `$` - matches the end of the line.

## Regex examples

identify any line with two or more vowels in a row

    user@bash: egrep '[aeiou]{2,}' mysampledata.txt
    Robert pears 4
    Lisa peaches 7
    Anne mangoes 7
    Greg pineapples 3

any line with a 2 on it which is not the end of the line

    user@bash: egrep '2.+' mysampledata.txt
    Fred apples 20

any line with the number 2 as the last character on the line

    user@bash: egrep '2$' mysampledata.txt
    Mark watermellons 12
    Susy oranges 12
    Oliver rockmellons 2

each line that contains either 'is or 'go' or 'or'

    user@bash: egrep 'or|is|go' mysampledata.txt
    Susy oranges 5
    Terry oranges 9
    Lisa peaches 7
    Susy oranges 12
    Anne mangoes 7

shows the orders of everyone whose name begins with A-K

    user@bash: egrep '^[A-K]' mysampledata.txt
    Fred apples 20
    Anne mangoes 7
    Greg pineapples 3
    Betty limes 14

# Activities

find every line with the word 'oranges' in it

    haleyharris$ egrep 'oranges' sampledata.txt
    Susy oranges 5
    Terry oranges 9
    Susy oranges 12

every line containing at least 2 numbers in a row

    haleyharris$ egrep '[0-9]{2,}' sampledata.txt
    Fred apples 20
    Mark watermellons 12
    Susy oranges 12
    Mark grapes 39
    Betty limes 14

case insensitive matching using `-i`

    haleyharris$ egrep -i '^A' sampledata.txt
    anne mangoes 7

    haleyharris$ egrep -i '^g' sampledata.txt
    GREG pineapples 3

case insensitive inverted matching - match lines that do not begin with A-K

    haleyharris$ egrep -iv '^[A-K]' sampledata.txt
    Susy oranges 5
    Mark watermellons 12
    Robert pears 4
    Terry oranges 9
    Lisa peaches 7
    Susy oranges 12
    Mark grapes 39
    Oliver rockmellons 2





