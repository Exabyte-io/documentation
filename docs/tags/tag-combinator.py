#!/usr/bin/env python

import os
import json


video_file=raw_input('Enter video file name in mp4 folder: ')
title=raw_input('Enter video title: ')
tags = raw_input('Enter JSON ID for tags list: ')


with open('tags.json') as json_file:
    python_obj = (json.load(json_file))

def retrieve_key(key):
  for i in range(len(python_obj)):
    if key in python_obj[i]:
       return python_obj[i][key]


tags_list= retrieve_key('@'+tags)

tags_list_1=[]
for i in range(len(tags_list)):
    if tags_list[i][0]=="@":
        tags_list_1.extend(retrieve_key(tags_list[i]))

tags_list=tags_list_1+tags_list
tags_list=[tags_list[i] for i in range(len(tags_list)) if '@' not in tags_list[i]]

os.system('youtube-upload --title="'+title+'"  --description="A.S.Mutter plays Beethoven"   --category="Science & Technology"  --tags="'+ ",".join(
    tags_list)+'"  --embeddable=True --privacy unlisted ../../scripts/mp4/'+video_file)
