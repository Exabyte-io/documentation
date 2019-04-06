#!/usr/bin/env python

import json
import os

import json_include


# first function: take original json and expand all tags in new json file #SCI-420
# second function: upload local video file to youtube if id is not present min original JSON, and update original JSON with id at the end
# third function: update metadata if id is present in original JSON


def flatten(initial_list):
    new_list = []
    for el in initial_list:
        tags = el["tags"]
        for el1 in tags:
            new_list.append(el1)
    return new_list


list_files = os.listdir("tutorials-metadata")

for i in range(len(list_files)):
    python_obj = json.loads(json_include.build_json("./", "tutorials-metadata/" + list_files[i]))
    print python_obj

    tags = python_obj["tags"]
    flattened_tags = flatten(tags)

    final_dict = {"tags": flattened_tags, "description": python_obj["description"],
                  "title": python_obj["title"]}

    with open('full-metadata/' + list_files[i], 'w') as outfile:
        json.dump(final_dict, outfile, indent=4)
