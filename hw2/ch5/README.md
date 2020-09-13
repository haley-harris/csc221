# Homework 2: Chapter 5: File Manipulation

## Creating directories

`mkdir` creates a directory

`mkdir -p` creates parent directories

`mkdir -v` tells you what mkdir is doing

## Removing directories

`rmdir` command removes directories

`rmdir` supports `-p` and `-v` options as well

if directory is not empty when `rmdir` is run, the directory will not be deleted

## Creating a blank file

`touch` checks if a file exists and creates a file if the one referred to does not exist

    touch README.md

`touch` can be used to modify file access and modification times on a file


## Copying a file or directory

`cp` can be used to duplicate files and directories

`cp` needs a file or directory to be copied and the location to copy to

    # copies the text file to the temp directory
    cp example.txt ~/Documents/temp


use `-r` recursive option to copy a directory and all of the files ad directories inside of it


## Move a file or directory

`mv` is used to move files and directories without having to use a recursive option

    # move example directory to the backup/temp directory
    mv example backup/temp

can also use `mv` command to rename files or directories by specifying the destination to be the same directory as the source but with a different name

## Removing files and non-empty directories

deleting files and directories with remove commands is permanent and cannot be undone in Linux

`rm` removes/deletes a file

`rm -r` can be used to delete directories and all files and directories contained within it

`-i` option will prompt you before removing each file and directory and gives an option to cancel the command









 

