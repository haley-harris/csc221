# Homework 2: Chapter 11: Piping and Redirection

Every program we run on the command line automatically has three data streams connected to it:

- STDIN (0) - Standard input (data fed into the program)
- STDOUT (1) - Standard output (data printed by the program, defaults to the terminal)
- STDERR (2) - Standard error (for error messages, also defaults to the terminal)

piping and redirection is the means by which we connect these streams between programs and files to direct data in interesting/useful ways

## Redirecting to a file

`>` (greater than operator) indicates to the command line taht we want to program's output to be saved in a file instead of printed on the screen

    user@bash: ls
    barry.txt bob example.png firstfile foo1 video.mpeg

    user@bash: ls > myoutput
    user@bash: ls
    barry.txt bob example.png firstfile foo1 myoutput video.mpeg

    user@bash: cat myoutput
    barry.txt
    bob
    example.png
    firstfile
    foo1
    myoutput
    video.mpeg

the format of data may be slightly different after piping or redirection, but it is still the same data

## Saving to an existing file

if you redirect to a file that does not exist, it will be automatically created

if you save into a file that already exists, the contents will be cleared and replaced by the new output being saved

    user@bash: cat myoutput
    barry.txt
    bob
    example.png
    firstfile
    foo1
    myoutput
    video.mpeg

    user@bash: wc -l barry.txt > myoutput
    user@bash: cat myoutput
    7 barry.txt


**append** data to existing files without deleting file's current content using `>>` operator

    user@bash: cat myoutput
    7 barry.txt

    user@bash: ls >> myoutput
    user@bash: cat myoutput
    7 barry.txt
    barry.txt
    bob
    example.png
    firstfile
    foo1
    myoutput
    video.mpeg


## Redirecting from a file

use `<` (less than operator) to send data the other way - read data from a file and feed it into the program via the STDIN stream


    user@bash: wc -l myoutput
    8 myoutput
    user@bash: wc -l < myoutput
    8

**combine two form of redirection** into a single command

    user@bash: wc -l < barry.txt > myoutput
    user@bash: cat myoutput
    7

## Redirecting STDERR

STDERR is streaming number 2

if a number is placed before the `>` operator, it will redirect the stream associated with the number

default number is stream 1

example of saving error message to a text file using stream 2 redirection

    user@bash: ls -l video.mpg blah.foo
    ls: cannot access blah.foo: No such file or directory
    -rwxr--r-- 1 ryan users 6 May 16 09:14 video.mpg
    
    user@bash: ls -l video.mpg blah.foo 2> errors.txt
    -rwxr--r-- 1 ryan users 6 May 16 09:14 video.mpg
    user@bash: cat errors.txt
    ls: cannot access blah.foo: No such file or directory

example of saving normal output and error messages in a single file: done by redirecting the STDERR stream to the STDOUT stream and redirecting STDOUT to a file

    user@bash: ls -l video.mpg blah.foo > myoutput 2>&1
    user@bash: cat myoutput
    ls: cannot access blah.foo: No such file or directory
    -rwxr--r-- 1 ryan users 6 May 16 09:14 video.mpg

## Piping

**piping** sends data from one program to another

`|` is the piping operator

example of using piping to list only the first 3 files in the directory

    user@bash: ls
    barry.txt bob example.png firstfile foo1 myoutput video.mpeg
    
    user@bash: ls | head -3
    barry.txt
    bob
    example.png

can pipe as many programs together as you like - the following gets only the third file

    user@bash: ls | head -3 | tail -1
    example.png

can combine piping and redirection

    user@bash: ls | head -3 | tail -1 > myoutput
    user@bash: cat myoutput
    example.png


# Activities

    haleyharris$ ls > filelist.txt
    haleyharris$ cat filelist.txt
    README.md
    ch1
    ch10
    ch11
    ch12
    ch13
    ch2
    ch3
    ch4
    ch5
    ch6
    ch7
    ch8
    ch9
    filelist.txt

    haleyharris$ ls ch10 > filelist.txt
    haleyharris$ cat filelist.txt
    README.md
    sampledata.txt

    haleyharris$ ls -l ch10 >> filelist.txt
    haleyharris$ cat filelist.txt
    README.md
    sampledata.txt
    total 16
    -rw-r--r--  1 haleyharris  staff  3265 Sep 15 16:25 README.md
    -rw-r--r--  1 haleyharris  staff   196 Sep 15 16:20 sampledata.txt

**list 20th from last file in etc directory**

    haleyharris$ ls /etc | tail -20 | head -1
    security
    

**count of files and directories that you have the execute permission fo in home directory**

    haleyharris$ ls -l ~ | grep -c '^...x'
    19
