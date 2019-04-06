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


list_files = []
parse_folder = os.listdir("../tutorials/")


for file in parse_folder:
    if file.endswith(".md"):
        if file[:].replace(".md", ".json") in parse_folder:
          list_files.append(file)

for i in range(len(list_files)):
    python_obj = json.loads(json_include.build_json("../tutorials", list_files[i].replace(".md", ".json")))

    tags = python_obj["tags"]
    flattened_tags = flatten(tags)

    final_dict = {"tags": flattened_tags, "description": python_obj["description"],
                  "title": python_obj["title"]}

    with open("../tutorials/"+list_files[i].replace(".md", "-expanded-metadata.json"), 'w') as outfile:
        json.dump(final_dict, outfile, indent=4)
