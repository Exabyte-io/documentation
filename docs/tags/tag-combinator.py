#!/usr/bin/env python

import json
import os

#video_file = raw_input('Enter video file name in mp4 folder: ')
#title = raw_input('Enter video title: ')
#tags = raw_input('Enter JSON ID for tags list: ')

with open('tutorials-metadata/kpt-convergence.json') as json_file:
        python_obj = (json.load(json_file))


print python_obj





#def retrieve_key(key):
#    key = key[1:]
#    with open(key + '.json') as json_file:
#        python_obj = (json.load(json_file))
#    return python_obj[0]['@' + key]


#tags_list = retrieve_key('@' + tags)

#tags_list_1 = []
#for i in range(len(tags_list)):
#    if tags_list[i][0] == "@":
#        tags_list_1.extend(retrieve_key(tags_list[i]))

#tags_list = tags_list_1 + tags_list
#tags_list = [tags_list[i] for i in range(len(tags_list)) if '@' not in tags_list[i]]
#print tags_list

#os.system(
#    'youtube-upload --title="' + title + '"  --description="A.S.Mutter plays Beethoven"   --category="Science & Technology"  --tags="' + ",".join(
#        tags_list) + '"  --embeddable=True --privacy unlisted ../../scripts/mp4/' + video_file)
