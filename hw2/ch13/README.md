# Homework 2: Chapter 13: Scripting

bash script allows us to define a series of actions which the computer will then perform without us having to enter the commands ourselves

`#!` known as **shebang** - is a path to the interpreter
- do **not** add spaces


## Important points

- the **very first line** of a script should tell the system which interpreter to be used on the file

use `which <program>` to find out where the interpreter is located

`#` are used in bash scripts for comments

typically include comments at the top of the script giving a description of what the script does, who wrote it and when

use `./` to override typical system behavior of ignoring the current directory - tells system to ignore the path and go straight to the location of the script

**by default you do not have execute permission of a bash script, even as the owner**

run `chmod 755 <script>` to ensure the script is set up properly

## Variables

- do not place spaces on either side of the `=` sign
- when you refer to a variable, place a `$` before the variable name

example:

    #!/bin/bash

    name='Ryan'
    echo Hello $name
    _______________________________

    user@bash: ./variableexample.sh
    Hello Ryan

variables that are automatically set for us:

- $0 - The name of the script.
- $1 - $9 - Any command line arguments given to the script. $1 is the first argument, $2 the second and so on.
- $# - How many command line arguments were given to the script.
- $* - All of the command line arguments.

## Back ticks

it is possible to save the output of a command to a variable using back ticks (`)

    #!/bin/bash

    lines=`cat $1 | wc -l`
    echo The number of lines in the file $1 is $lines
    __________________________________________________

    user@bash: ./backticks.sh testfile.txt
    The number of lines in the file testfile.txt is 12

## if statements

