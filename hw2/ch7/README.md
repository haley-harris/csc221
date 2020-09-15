# Homework 2: Chapter 7: Wildcards

**wildcards** are a set of building blocks that allow you to create a pattern defining a set of files or directories

## Basic set of wildcards:
- `*` represents zero (0) or more characters
- `?` represents a single character
- `[]` represents a range of characters

## Under the hood

- bash translates wildcards and replaces the pattern with every file or directory that matches
- wildcards work on relative and absolute paths

## Examples of * wildcard

    user@bash: ls
    barry.txt blah.txt bob example.png firstfile foo1 foo2
    foo3 frog.png secondfile thirdfile video.mpeg
    user: ls b*
    barry.txt blah.txt bob

    user@bash: ls /home/ryan/linuxtutorialwork/*.txt
    /home/ryan/linuxtutorialwork/barry.txt /home/ryan/linuxtutorialwork/blah.txt

## ? operator

    user@bash: ls ?i*
    firstfile video.mpeg

`?i*` searches for all paths with at least one instance of the 'i' character in its name

    user@bash: ls *.???
    barry.txt blah.txt example.png frog.png

`*.???` matches every file with 3 letter extension

## [] operator

limits range to a subset of characters

    user@bash: ls [sv]*
    secondfile video.mpeg

`[sv]*` looks for every file or directory that begins with either an s or a v


    user@bash: ls *[0-9]*
    foo1 foo2 foo3

`*[0-9]*` uses hypen to specify a range - finds every file with a digit in its name

    user@bash: ls [^a-k]*
    secondfile thirdfile video.mpeg

`^` reverses a range - meaning look for any character which is not one of the following

## Examples

find the file type of every file in a directory

    user@bash: file ~/Documents/belhavencsc/csc221/*
    README.md: ASCII text
    hw1: directory
    hw2: directory

move all file types of either jpg or png into another directory


    user@bash: mv public_html/*.??g public_html/images/

find size and mod time of .bash_history file in every user's home directory

**.bash_history** file keeps a history of commands user has entered on the command line

    user@bash: ls -lh /Users/*/.bash_history
    -rw-------  1 haleyharris  staff   8.0K Sep 13 15:49 /Users/haleyharris/.bash_history

# Activities

**list files that contain an extension**

    bash-3.2$ ls *.*


**list files with only a 3 letter extension**

    bash-3.2$ ls *.???
    afpovertcp.cfg


**files that have only 4 characters in the name**

    bash-3.2$ ls ????.*
    find.codes	find.codes~orig	krb5.keytab	mail.rc		
    mail.rc~orig


**a file that contains an uppercase letter in its name**

    bash-3.2$ ls *[A-Z]*
    bashrc_Apple_Terminal
