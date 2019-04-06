#!/usr/bin/env python

import json
import os

import json_include


def flatten(initial_list):
    new_list = []
    for el in initial_list:
        tags = el["tags"]
        for el1 in tags:
            new_list.append(el1)
    return new_list


list_files = [
    os.path.join(root, file)
    for root, dirs, files in os.walk("../tutorials/")
    for file in files
    if file.endswith(".md")
    if file[:].replace(".md", ".json") in files
]

for i in range(len(list_files)):
    python_obj = json.loads(json_include.build_json("./", list_files[i][:].replace(".md", ".json")))

    tags = python_obj["tags"]
    flattened_tags = flatten(tags)

    final_dict = {"tags": flattened_tags, "description": python_obj["description"],
                  "title": python_obj["title"]}

    with open("../tutorials/" + list_files[i][:].replace(".md", "-expanded-metadata.json"), 'w') as outfile:
        json.dump(final_dict, outfile, indent=4)
