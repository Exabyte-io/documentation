#!/usr/bin/python

import os
import json
import googleapiclient.discovery

from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload
from oauth2client.tools import argparser, run_flow
from oauth2client.client import flow_from_clientsecrets
from utils import flatten, update_metadata, parseIncludeStatements

SCOPE = "https://www.googleapis.com/auth/youtube"
CLIENT_SECRETS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "secrets.json"))


def get_credentials():
    """
    Returns the credentials to establish connection to YouTube API.
    """
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPE)
    storage = Storage("credentials.json")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return credentials


def get_youtube_api_client():
    """
    Returns YouTube API client.
    """
    return googleapiclient.discovery.build("youtube", "v3", credentials=get_credentials())


def get_category_id(youtube_, category):
    """
    Returns the ID of a given category.

    Args:
        youtube_: YouTube API client instance
        category (str): category to get the ID for.

    Returns:
         str
    """
    categories = youtube_.videoCategories().list(part="snippet", regionCode="US").execute()["items"]
    return next((c["id"] for c in categories if c["snippet"]["title"] == category))


def get_video_body_param(youtube_, metadata_):
    """
    Returns the body of the the request to YouTube API.
    Args:
        youtube_: YouTube API client instance.
        metadata_ (dict): video metadata.

    Returns:
         dict
    """
    return json.loads(json.dumps({
        "snippet": {
            "title": metadata_["title"],
            "tags": metadata_.get("tags", []),
            "description": metadata_["description"],
            "categoryId": get_category_id(youtube_, metadata_.get("category", "Science & Technology")),
        },
        "status": {
            "privacyStatus": metadata_.get("privacy", "private")
        }
    }))


def insert_video(youtube_, file_, metadata_):
    """
    Uploads a given video.

    Args:
        youtube_: YouTube API client instance
        file_ (str): path to the video file.
        metadata_ (dict): video metadata.

    Returns:
         dict
    """
    body = get_video_body_param(youtube_, metadata_)
    return youtube_.videos().insert(body=body, part=",".join(body.keys()), media_body=MediaFileUpload(file_)).execute()


def update_video(youtube_, metadata_):
    """
    Updates video metadata.

    Args:
        youtube_: YouTube API client instance
        metadata_ (dict): video metadata.

    Returns:
         dict
    """
    body = get_video_body_param(youtube_, metadata_)
    body["id"] = metadata["youTubeId"]
    return youtube_.videos().update(body=body, part=",".join(body.keys())).execute()


if __name__ == '__main__':
    argparser.add_argument('-f', '--file', required=True, help='video file path')
    argparser.add_argument('-m', '--metadata', required=True, help='video metadata file path')
    args = argparser.parse_args()

    if not os.path.exists(args.file): exit("video file does not exist!")
    if not os.path.exists(args.metadata): exit("metadata file does not exist!")

    youtube = get_youtube_api_client()
    metadata = parseIncludeStatements(args.metadata)
    metadata["tags"] = flatten(metadata["tags"])
    if not metadata.get("youTubeId"):
        youTubeId = json.dumps(insert_video(youtube, args.file, metadata), indent=4)["id"]
        update_metadata(args.metadata, {"youTubeId": youTubeId})
    else:
        update_video(youtube, metadata)
