# Part 1

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
<br>
<br>

# Part 2

## Task 1: Produce a sorted text file

    haleyharris$ sort shuffled-words.txt > shuffled-words-sorted.txt

* `sort` alphabetically sorts the 'shuffled-words.txt' file
* `>` redirects sorted output into a new file called 'shuffled-words-sorted.txt'


## Task 2: Find the 10 most common words in a text file

    haleyharris$ sort rand-words.txt | uniq -c | sort -nr |head -10 > common-words.txt

* `sort` alphabetically sorts 'rand-words.txt' for `uniq` to work properly
* `uniq -c` counts word frequency 
* `sort -nr` is a numerical reverse sort - `uniq -c` ouput is not sorted
    * numerical sorting begins with the lowest number - reverse sorting begins with largest number
    * if `-n` option is not used, sort will be based on lowest starting digit, not the actual lowest number
* `head -10` will output first 10 words and word counts - which should be the 10 most common words in the text file after sorting
* `>` redirects output into a new file called 'common-words.txt'

## Task 3: Find 10 most common numbers in a text file

    haleyharris$ sort rand-numbers.txt | uniq -c | sort -nr| head -10 > common-numbers.txt


* `sort` will sort numbers in 'rand-numbers.txt' so uniq will work properly
* `uniq -c` counts frequency of repeated numbers
* `sort -nr` numerically reverse sorts numbers from largest `uniq` frequency number to the smallest
* `head -10` prints first 10 (and most common) numbers
* `>` redirects output for the 10 most common numbers into new file called 'common-numbers.txt'