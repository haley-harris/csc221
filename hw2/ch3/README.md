# Homework 3: Chapter 3: Files

everything in Linux is a file (text file, directory, monitor, keyboard)


## Linux is an extionless system:
- system ignores extensions and looks inside the file to determine what
  type of file it is
- `file` command is used to show file type


## Linux is case sensitive:
- FILE.txt File.txt and file.txt are all different files in the Linux  
  system


## when dealing with files that have spaces in the name:

- put the file name in quotes

    `cd 'Holiday Photos'`

- use escape characters

    `cd Holiday\ Photos`

## Hidden files and directories

- if a file or directory's name starts with `.` it is considered to be hidden

- to view hidden files/directories use `ls -a` command