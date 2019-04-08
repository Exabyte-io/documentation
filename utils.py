import os
import json
import json_include


def parseIncludeStatements(file_path):
    """
    Resolves `include` statements.

    Args:
        file_path (str): file to parse.

    Returns:
         dict|list
    """
    dirName = os.path.dirname(file_path)
    baseName = os.path.basename(file_path)
    return json.loads(json_include.build_json(dirName, baseName))


def get_metadata(metadata_path):
    return parseIncludeStatements(metadata_path)


def update_metadata(metadata_path, data):
    with open(metadata_path, 'r+') as f:
        metadata = json.loads(f.read())
        metadata.update(data)
        f.seek(0)
        f.truncate()
        f.write(json.dumps(metadata, indent=4))


def flatten(data):
    list_ = []
    if isinstance(data, list):
        [list_.extend(flatten(item)) for item in data]
    elif isinstance(data, dict):
        [list_.extend(flatten(item)) for item in data.values()]
    else:
        list_.append(data)
    return list_
