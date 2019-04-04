#!/usr/bin/env python

import json
import os

import json_include

video_file = raw_input('Enter video file name in mp4 folder: ')
title = raw_input('Enter video title: ')
tags = raw_input('Enter JSON ID in tutorials-metadata folder for tags list: ')

python_obj = (json.loads(json_include.build_json("./", "tutorials-metadata/" + tags + ".json")))
list_tags = python_obj[1]
list_tags = [list_tags[i].values() for i in range(len(list_tags))]
list_tags = [y for x in list_tags for y in x]

print list_tags

os.system(
    'youtube-upload --title="' + title + '"  --description="A.S.Mutter plays Beethoven"   --category="Science & Technology"  --tags="' + ",".join(
        list_tags) + '"  --embeddable=True --privacy unlisted ../../scripts/mp4/' + video_file)
