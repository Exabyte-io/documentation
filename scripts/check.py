#!/usr/bin/env python2.7

import os
import sys

# extract pathnames of all .md files in documentation
list_files = []
for root, dirs, files in os.walk("/Users/exabyteinc/Code/exabyte-public-documentation/docs"):
    for file in files:
        if file.endswith(".md"):
            list_files.append(os.path.join(root, file))

list_files_copy = []

IMAGES_PATH = "/Users/exabyteinc/Code/exabyte-public-documentation/docs/images/"
for path in list_files:
    print path
    relative_path = os.path.relpath(IMAGES_PATH, os.path.dirname(path))
    print relative_path
    with open(path, "r+") as f:
        content = f.read()
        content = content.replace('/images', relative_path)
        f.seek(0)
        f.write(content)

sys.exit()

for filex in list_files_copy:

    if selection == 1:
        # assert second-degree headers in pages
        n = 0
        file_open = open(filex)
        list_lines = file_open.readlines()
        for i in range(len(list_lines) - 1):
            if len(list_lines[i].split()) > 0 and list_lines[i].split()[0] == '#' and list_lines[i + 1].strip() == '':
                n = n + 1
        if n > 1:
            print filex


    elif selection == 2:
        # Make sure links are relative
        for i in range(len(list_lines)):
            if r'(/' in list_lines[i] and list_lines[i].split('/')[1].strip() != 'images':
                print filex


    elif selection == 3:
        # make headers in "overview.md" files to be links
        n = 0
        for i in range(len(list_lines)):
            if len(list_lines[i].split()) > 0 and '##' in list_lines[i].split()[0] and '[' not in list_lines[
                i] and ']' not in list_lines[i] and n == 0 and 'inks' not in list_lines[i]:
                print filex
                n = n + 1


    elif selection == 4:
        # Fix links with new notation like [^1]
        n = 0
        for i in range(len(list_lines)):
            if r'(#link' in list_lines[i] and n == 0:
                print filex
                n = n + 1


    elif selection == 5:
        for i in range(len(list_lines)):
            if r'images/' in list_lines[i]:
                path_img = list_lines[i].split('images/')[1].split()[0].strip('" > /')
                dir_name = filex.split('docs/')[1].split('/')[0]
                os.system(
                    "cd /Users/exabyteinc/Code/exabyte-public-documentation/docs/images; mkdir " + dir_name + "; cp " + path_img + " " + dir_name)
