#!/usr/bin/env python3
''' Regex Search

Author: Haley Harris
'''
import argparse, re, os
from pathlib import Path

def regex_search(folder_path, regex):
    '''Given a path to a folder, opens all .txt files in a folder and
    searches for any line that matches a user-supplied regular
    expression. Returns all lines that contain the given regular
    expression.

    Args:
      folder_path (str): Path to a folder in the file system
      regex (str): Regular expression (as a string)

    Returns:
      list: List of all lines containing the regular expression

    '''
    
    folder_path = Path(str(folder_path))
    txt_files = list(folder_path.glob('*.txt'))

    list_of_matches = []

    for files in txt_files:

       content = open(files, 'r')
       lines = content.readlines()
       
       for line in lines:
            search_txt_regex = re.compile(regex)
            regex_match = re.findall(search_txt_regex, line)

            if regex_match:
                list_of_matches.append(line)

    return list_of_matches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to search for .txt files')
    parser.add_argument('regex', help='Regular expression to search for')

    args = parser.parse_args()

    for line in regex_search(args.folder, args.regex):
        print(line)

if __name__=='__main__':
    main()


