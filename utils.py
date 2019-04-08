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


def update_metadata(metadata_path, data):
    """
    Updates metadata with given data and stores it back.

    Args:
        metadata_path (str): path to the metadata file.
        data (dict): the data to update metadata with.
    """
    with open(metadata_path, 'r+') as f:
        metadata = json.loads(f.read())
        metadata.update(data)
        f.seek(0)
        f.truncate()
        f.write(json.dumps(metadata, indent=4))


def flatten(data):
    """
    Flattens the given data structure.

    Returns:
         list[str]
    """
    list_ = []
    if isinstance(data, list):
        [list_.extend(flatten(item)) for item in data]
    elif isinstance(data, dict):
        [list_.extend(flatten(item)) for item in data.values()]
    else:
        list_.append(data)
    return list_
