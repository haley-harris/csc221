# Homework 2: Chapter 8: Permissions

## Permissions

- `r` - read - you may view the contents of the file
- `w` - write - you may change the contents of the file
- `x` - execute - you may execute or run the file if it is a program or script

- **owner** - single person who owns the file
- **group** - every file belongs to a single group
- **others** - everyone else who is not in the group or the owner


## View permissions

`ls -l [path]` shows permissions for each file

    user@bash: ls -l /home/ryan/linuxtutorialwork/frog.png
    -rwxr----x 1 harry users 2.7K Jan 4 07:32 /home/ryan/linuxtutorialwork/frog.png

first character identifies file type:
- if it starts with a `-` it is a normal file
- if it starts with a `d` it is a directory

the following 3 characters represent the permission for the **owner**
- a letter represents the presence of a permission
- a `-` represents the absence of a permission

the next 3 characters represent the permissions for the **group**

the last 3 characters represent the permissions for **others**

## Change permissions

`chmod [permissions][path]` (change file mode bits) command changes permissions on a file or directory

3 components of `chmod` permission arguments:
- who are we changing permissions for
    - `u` - user (owner)
    - `g` - group
    - `o` - other
    - `a` - all
- are we granting or revoking the permission
    - `+` - granting permission
    - `-` - revoking permission
- which permission are we setting
    - `r` - read
    -  `w` - write
    - `x` - execute

## Examples

grant the execute permission to the group

    user@bash: ls -l frog.png
    -rwxr----x 1 harry users 2.7K Jan 4 07:32 frog.png

    user@bash: chmod g+x frog.png
    user@bash: ls -l frog.png
    -rwxr-x--x 1 harry users 2.7K Jan 4 07:32 frog.png

remove the write permission for the owner

    user@bash: chmod u-w frog.png
    user@bash: ls -l frog.png
    -r-xr-x--x 1 harry users 2.7K Jan 4 07:32 frog.png

can assign multiple permissions at one time

    user@bash: ls -l frog.png
    -rwxr----x 1 harry users 2.7K Jan 4 07:32 frog.png

    # add write and execute permissions for group
    user@bash: chmod g+wx frog.png
    user@bash: ls -l frog.png
    -rwxrwx--x 1 harry users 2.7K Jan 4 07:32 frog.png

    # revoke execute permission from group and others
    user@bash: chmod go-x frog.png
    user@bash: ls -l frog.png
    -rwxrw---- 1 harry users 2.7K Jan 4 07:32 frog.png


shorthand methods to set permission


| Octal |	Binary |
| -----| --------|
| 0	   |    0 0 0  |
| 1	   |    0 0 1  |
| 2	   |    0 1 0  |
| 3	   |    0 1 1  |
| 4	   |    1 0 0  |
| 5	   |    1 0 1  |
| 6	   |    1 1 0  |
| 7	   |    1 1 1  |


## Setting permissions with octal values

    user@bash: ls -l frog.png
    -rw-r----x 1 harry users 2.7K Jan 4 07:32 frog.png

    user@bash: chmod 751 frog.png
    user@bash: ls -l frog.png
    -rwxr-x--x 1 harry users 2.7K Jan 4 07:32 frog.png

    user@bash: chmod 240 frog.png
    user@bash: ls -l frog.png
    --w-r----- 1 harry users 2.7K Jan 4 07:32 frog.png


## Permissions for directories

the same permissions may be used for directories but have slightly different behaviors

- `r` - have the ability ot read contents of directory (do an ls)
- `w` - have the ability to write into the directory (create files and directories)
- `x` - have the ability to enter the directory (cd)

examples: 

    user@bash: ls testdir
    file1 file2 file3

    user@bash: chmod 400 testdir
    ls -ld testdir
    dr-------- 1 ryan users 2.7K Jan 4 07:32 testdir

    user@bash cd testdir
    cd: testdir: Permission denied

    user@bash: ls testdir
    file1 file2 file3
    
    user@bash: chmod 100 testdir
    ls -ld testdir
    ---x------ 1 ryan users 2.7K Jan 4 07:32 testdir
    
    user@bash ls testdir
    user@bash: cd testdir
    user@bash: pwd
    /home/ryan/testdir
    ls: cannot open directory testdir/: Permission denied


`ls -ld` lists permissions for the specified directory

if you have the read permission on files within a directory that does not have a read permission, you can still read the files within if you know the file name

## Root user

on Linux, typically the only people who can change the permissions of a file or directory are the **owner** of the file/directory or the **root user**

typically only administrators have access to the root account

normal users have access to files and directories in their home directory


# Activities

**file permissions**

    haleyharris$ ls -l b.txt
    -rw-r--r--  1 haleyharris  staff   0 Sep 14 22:30 b.txt

    haleyharris$ chmod o-r b.txt
    -rw-r-----  1 haleyharris  staff   0 Sep 14 22:30 b.txt

    haleyharris$ chmod a-w b.txt
    -r--r-----  1 haleyharris  staff   7 Sep 14 22:33 b.txt

    haleyharris$ echo 'try to write' > b.txt
    -bash: b.txt: Permission denied


**directory permissions**

    haleyharris$ ls -ld temp
    drwxr-xr-x  5 haleyharris  staff  160 Sep 14 22:39 temp

    haleyharris$ chmod a-rw temp | ls -ld temp
    d--x--x--x  7 haleyharris  staff  224 Sep 14 22:47 temp


**etc file and directory permissions**

    drwxr-xr-x  11 root  wheel     352 Oct 24  2018 apache2
    -r--r--r--   1 root  wheel     265 Aug 17  2018 bashrc
    -rw-r--r--@  1 root  wheel      22 Jul 22  2018 ntp.conf

**bin file permissions**

    -r-xr-xr-x  1 root  wheel   618416 Sep 20  2018 bash
    -rwxr-xr-x  1 root  wheel    18128 Sep 20  2018 echo
    -r-xr-xr-x  1 root  wheel   618480 Sep 20  2018 sh

















