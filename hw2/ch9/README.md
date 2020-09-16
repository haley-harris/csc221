# Homework 2: Chapter 9: Filters

a **filter** is a program that accepts textual data and transforms it in a particular way. they take raw data and manipulate it to be displayed in a way more suited to what you're after


## head

**head** is a program that prints x number of lines of its input - by default it prints first 10 lines but can be modified

`head [-number of lines to print][path]`

    user@bash: head -4 mysampledata.txt
    Fred apples 20
    Susy oranges 5
    Mark watermellons 12
    Robert pears 4

## tail

**tail** prints the last x number of lines of its input

`tail [-number of lines to print][path]`

    user@bash: tail -3 mysampledata.txt
    Greg pineapples 3
    Oliver rockmellons 2
    Betty limes 14


## sort

**sort** sorts it input - alphabetically by default

`sort [-options][path]`

    user@bash: sort mysampledata.txt
    Anne mangoes 7
    Betty limes 14
    Fred apples 20
    Greg pineapples 3
    Lisa peaches 7
    Mark grapes 39
    Mark watermellons 12

## nl

**nl** stands for number lines and numbers the lines

`nl [-options][path]`

    user@bash: nl mysampledata.txt
    1 Fred apples 20
    2 Susy oranges 5
    3 Mark watermellons 12
    4 Robert pears 4
    5 Terry oranges 9 


## wc

**wc** stands for word count and counts words as well as characters and lines and gives a count of each (lines words char)

`wc [-options][path]`

    user@bash: wc mysampledata.txt
    12 36 195 mysampledata.txt


## cut

**cut** is useful for content that is separated into fields (columns) 

`cut [-options][path]`

example is taking first column from sample data with three columns

    user@bash: cut -f 1 -d ' ' mysampledata.txt
    Fred
    Susy
    Mark
    Robert

- cut defaults to using tab separator to identify fields, but can be changed
- `-d` is used to specify separator character
- `-f` is used to specify which field (column) we want

## sed

**sed** stands for stream editor and allows you to do a search and replace on data

`sed <expression>[path]`

basic expression example:

- s/search/replace/g
    - **s** stands for substitute and specifies the action to perform
    - place the word to search for where /**search**/ is in example
    - place the replacement word where /**replace**/ is in example
    - **g** stands for global


## uniq

**uniq** removes duplicate lines from data however *lines must be adjacent*

`uniq [options][path]`


## tac

**tac** reverse cat - prints last line first - prints file backwards line-by-line

`tac [path]`

# Activities

**head command**

    haleyharris$ head -2 sampledata.txt
    Fred apples 20
    Susy oranges 5

**tail command**

    haleyharris$ tail -3 sampledata.txt
    Greg pineapples 3
    Oliver rockmellons 2
    Betty limes 14

**sort command**

    haleyharris$ sort sampledata.txt
    Anne mangoes 7
    Betty limes 14
    Fred apples 20
    Greg pineapples 3
    Lisa peaches 7
    Mark grapes 39

**nl command**

    haleyharris$ nl sampledata.txt
        1	Fred apples 20
        2	Susy oranges 5
        3	Susy oranges 5
        4	Susy oranges 5
        5	Mark watermellons 12

**wc command**

    haleyharris$ wc sampledata.txt
    13      42     226 sampledata.txt

    haleyharris$ wc -lc sampledata.txt
    13     226 sampledata.txt

**cut command**

    haleyharris$ cut -f 1 -d ' ' sampledata.txt
    Fred
    Susy
    Susy
    Mark

    haleyharris$ cut -f 2,3 -d ' ' sampledata.txt
        apples 20
    oranges 5
    oranges 5
    watermellons 12


**sed command**

    haleyharris$ cat sampledata.txt
    Mark watermellons 12
    Oliver rockmellons 2

    haleyharris$ sed 's/mellons/melons/g' sampledata.txt
    Mark watermelons 12
    Oliver rockmelons 2

**uniq command**

    haleyharris$ cat sampledata.txt
    Susy oranges 12
    Mark grapes 39
    Mark grapes 39
    Anne mangoes 7

    haleyharris$ uniq sampledata.txt
    Susy oranges 12
    Mark grapes 39
    Anne mangoes 7

sort in reverse using `-r` option

    haleyharris$ sort -r sampledata.txt
    Terry oranges 9
    Susy oranges 5
    Susy oranges 12
    Robert pears 4
    Oliver rockmellons 2

nl incrementing using `-i <number>`

    haleyharris$ nl -i 2 sampledata.txt
    1	Fred apples 20
    3	Susy oranges 5
    5	Susy oranges 5
    7	Mark watermellons 12