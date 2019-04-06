#!/usr/bin/env python

import collections
import json
import os

import json_include

video_file = raw_input('Enter video file name in mp4 folder: ')
title = raw_input('Enter video title: ')
tags = raw_input('Enter tutorial name in tutorials-metadata folder for tags list: ')

python_obj = ((json.loads(json_include.build_json("./", "tutorials-metadata/" + tags + ".json")))["tags"])

list_tags = [d['...'] for d in python_obj]


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el


list_tags = list(flatten(list_tags))

print list_tags

os.system(
    'youtube-upload --title="' + title + '"  --description="A.S.Mutter plays Beethoven"   --category="Science & Technology"  --tags="' + ",".join(
        list_tags) + '"  --embeddable=True --privacy unlisted ../../scripts/mp4/' + video_file)
