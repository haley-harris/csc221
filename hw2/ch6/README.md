# Homework 2: Chapter 6: Vi Text Editor

Vi is a command line text editor

## two modes in Vi:
- **insert(input)** - enter content into the file
- **edit** - can move around the file, perform actions like deleting, copying, search & replace, saving, etc.

to run Vi use the `vi` command with the name of the file to be edited

    vi <filename>

## Modes 

- vi always starts in edit mode

- switch to insert mode by pressing `i`

- bottom left corner shows --INSERT-- 

- press `ESC` to get back to edit mode

## Saving and Exiting

- `ZZ` - save and exit
- `:q!` - discard all changes since last save and exit
- `:w` - save file but don't exit
- `:wq` - save and exit

## Ways to view files

- `cat` (concatenate) can be used to view file content
- `less` is better for larger files as it allows you to page through file content using `SPACE` for foward and `b` for back


## Navigating a file in Vi

- Arrow keys - move the cursor around
- j, k, h, l - move the cursor down, up, left and right (similar to the arrow keys)
- ^ (caret) - move cursor to beginning of current line
- $ - move cursor to end of the current line
- nG - move to the nth line (eg 5G moves to 5th line)
- G - move to the last line
- w - move to the beginning of the next word
- nw - move forward n word (eg 2w moves two words forwards)
- b - move to the beginning of the previous word
- nb - move back n word
- { - move backward one paragraph
- } - move forward one paragraph

**`:set nu`** in edit mode will enable line numbers

## Deleting Content

- x - delete a single character
- nx - delete n characters (eg 5x deletes five characters)
- dd - delete the current line
- dn - d followed by a movement command. Delete to where the movement command would have taken you. (eg d5w means delete 5 words)


## Undoing

- u - Undo the last action (you may keep pressing u to keep undoing)
- U (Note: capital) - Undo all changes to the current line

## Other vi actions

- copy and paste
- search and replace
- buffers
- markers
- ranges
- settings