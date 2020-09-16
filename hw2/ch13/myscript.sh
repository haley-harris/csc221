#!/bin/bash
# demo script



echo 'Number of files in this directory'
find . -type f | wc -l

echo 'Number of directories in this directory'
find . -mindepth 1 -type d | wc -l

echo 'The largest file in this directory'
du -a . | sort -nr | head -n 2

echo 'Last modified file'
find .  -type f | ls -lt | head -n 2
