#!/usr/bin/python

import os
import json
import googleapiclient.discovery

from jinja2 import Template
from google.cloud import texttospeech
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from oauth2client.client import flow_from_clientsecrets
from utils import flatten, update_metadata, parseIncludeStatements
from googleapiclient.http import MediaFileUpload, MediaInMemoryUpload

SCOPE = "https://www.googleapis.com/auth/youtubepartner"
CLIENT_SECRETS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "oauth-key.json"))
DESCRIPTION_TEMPLATE = os.path.abspath(os.path.join(os.path.dirname(__file__), "video-description.jinja"))
SERVICE_ACCOUNT_KEY_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "service-account-key.json"))
DESCRIPTION_LINKS = [
    "Materials Modeling 2.0: https://exabyte.io/",
    "Exabyte.io Platform: https://platform.exabyte.io/",
    "Exabyte.io Documentation: https://docs.exabyte.io/",
]

LANGUAGE_CODE = 'en-US'
AUDIO_ENCODING = texttospeech.enums.AudioEncoding.MP3
SSML_GENDER = texttospeech.enums.SsmlVoiceGender.NEUTRAL


def get_oauth_credentials():
    """
    Returns the credentials to establish connection to YouTube API.
    """
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPE)
    storage = Storage("oauth-credentials.json")
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)
    return credentials


def get_text_to_speech_api_client():
    """
    Returns TextToSpeech API client.
    """
    return texttospeech.TextToSpeechClient.from_service_account_file(SERVICE_ACCOUNT_KEY_FILE)


def get_youtube_api_client():
    """
    Returns YouTube API client.
    """
    return googleapiclient.discovery.build("youtube", "v3", credentials=get_oauth_credentials())


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
            "privacyStatus": metadata_["privacyStatus"]
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


def create_svb_caption_content(metadata_):
    """
    Creates SubViewer caption content from metadata.

    See https://support.google.com/youtube/answer/2734698 for more information.

    Args:
        metadata_ (dict): video metadata.

    Returns:
        str
    """
    return ["".join((c["startTime"], ",", c["endTime"], "\n", c["text"])) for c in metadata_["youTubeCaptions"]]


def insert_caption(youtube_, youTubeId_, name, content):
    """
    Creates a caption from metadata and inserts it to YouTube.

    Args:
        youtube_: YouTube API client instance.
        youTubeId_: the ID of video.
        name (str): caption name.
        content (str): caption content.
    """
    request = youtube_.captions().insert(
        part="snippet",
        body={
            "snippet": {
                "language": LANGUAGE_CODE,
                "name": name,
                "videoId": youTubeId_
            }
        },
        media_body=MediaInMemoryUpload("\n".join(content))
    )
    return request.execute()


def create_SSML_text(metadata_):
    """
    Creates SSML text from metadata.

    See https://cloud.google.com/text-to-speech/docs/ssml for more information.
    Args:
        metadata_ (dict): video metadata.

    Returns:
        str
    """
    pass


def convert_text_to_speech(text, speech_path):
    """
    Converts a given text to speech.

    Args:
        text (str): SSML text
        speech_path (str): path to store the audio file.
    """
    client = get_text_to_speech_api_client()
    synthesis_input = texttospeech.types.SynthesisInput(text=text)
    voice = texttospeech.types.VoiceSelectionParams(language_code=LANGUAGE_CODE, ssml_gender=SSML_GENDER)
    audio_config = texttospeech.types.AudioConfig(audio_encoding=AUDIO_ENCODING)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open(speech_path, 'wb') as out:
        out.write(response.audio_content)


if __name__ == '__main__':
    group = argparser.add_mutually_exclusive_group()
    argparser.add_argument('-f', '--file', required=True, help='video file path')
    argparser.add_argument('-m', '--metadata', required=True, help='video metadata file path')
    group.add_argument('--update', action="store_true", help='whether to update the video')
    group.add_argument('--upload', action="store_true", help='whether to upload the video')
    group.add_argument('--voiceOver', action="store_true", help='whether to add audio to the video')
    argparser.add_argument('-p', '--privacyStatus', default="unlisted", help='video privacy status')
    args = argparser.parse_args()

    if not os.path.exists(args.file): exit("video file does not exist!")
    if not os.path.exists(args.metadata): exit("metadata file does not exist!")

    # extract metadata
    metadata = parseIncludeStatements(args.metadata)
    metadata["tags"] = flatten(metadata["tags"])
    metadata["privacyStatus"] = metadata.get("privacyStatus", args.privacyStatus)
    metadata["descriptionLinks"] = metadata.get("descriptionLinks", []) + DESCRIPTION_LINKS
    with open(DESCRIPTION_TEMPLATE) as f:
        metadata["description"] = Template(f.read()).render(**metadata)

    youtube = get_youtube_api_client()

    if args.update:
        if not metadata.get("youTubeId"): exit("metadata does not contain youTubeId!")
        update_video(youtube, metadata)

    if args.upload:
        youTubeId = insert_video(youtube, args.file, metadata)["id"]
        caption_content = create_svb_caption_content(metadata)
        insert_caption(youtube, youTubeId, metadata["title"], caption_content)
        update_metadata(args.metadata, {"youTubeId": youTubeId})

    if args.voiceOver:
        pass
