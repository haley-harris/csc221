## How to search and find specific words contained in multiple files within a directory and how to move the identified files into a different directory
<br>

## Example:

You are given a directory that contains 200 files all starting with the letter 'f' and you wish to find out how many of the files contain a specific word (the word in this example being 'abducting')

-----------------------------------------------------------------


To find which files in the current directory contain the word 'abducting' use the `grep` command with the following format:

    haleyharris$ grep -l abducting f*

* `-l` option will print the filename of each file containing the word 'abducting'

* `abducting` is the word grep will search for

* Placing `f` in front of the `*` wildcard will only search inside files whose names begin with the letter 'f' (if `*` is used on its own, all files in the directory will be searched)

-----------------------------------------------------------------

Using command substitution with `mv` allows you to move all files containing the word 'abducting' into a different directory using only one shortened command instead of typing out each individual filename to be moved

**Relative path example**

    haleyharris$ mv $(grep -l abducting f*) ../abducting

**Absolute path example**

    haleyharris$ mv $(grep -l abducting f*) /Users/haleyharris/Desktop/belhavencsc/csc221/hw3/abducting


* Using command substitution allows you to feed the filenames to `mv` based on the output of the grep command - which tells `mv` exactly which files should be moved to the abducting directory

* `mv` is the command used to move or rename files
* `$()` is used for command substitution - the output of the command will replace the command itself
* `grep -l abducting f*` searches for occurrences of a word across multiple files
* `../abducting` is the destination directory for all files found by the grep command 
