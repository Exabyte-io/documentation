#!/usr/bin/env python
"""
Simple command-line example for Google Translate API.

https://developers.google.com/api-client-library/python/apis/translate/v2
"""

# TODO - the current logic should be adjusted to avoid translation of:
#   - markdown links [X](https://x.com)
#   - source code between ``` ```
#   - admonitions "!!!note"

from __future__ import print_function
import sys
import argparse
import errno
import os
import io
from googleapiclient.discovery import build

# Top-level directory for multiple languages
LANGUAGE_DIR_PREFIX = 'lang'
DEFAULT_LANGUAGE_CODE = 'ja'
# Number of new files to translate / API requests.
# Total number of files in repo is ~1600 as of 2019-02.
DEFAULT_THRESHOLD = 10
# Google API key to communicate with Cloud Translate API
# DO NOT COMMIT
GOOGLE_API_KEY = ''

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threshold', nargs='?', type=int, dest='threshold')
parser.add_argument('-i', '--input-path', action="store", dest='input_path', help="input path")
parser.add_argument('-l', '--languade-code', action="store", dest='language_code', help="language code ISO_639-1")
args = parser.parse_args()


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def get_file_as_array(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def get_file_as_text(filename):
    with io.open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def translate_array(array, language_code):
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build('translate', 'v2',
              developerKey=GOOGLE_API_KEY)
    translations = service.translations().list(
        source='en',
        target=language_code,
        # format="text",
        q=array
      ).execute()['translations']
    return list(map(lambda x: x['translatedText'], translations))

def write_array_as_file(array, filename):
    with open(filename, "w+") as f1:
        f1.write("\n".join(array).encode('utf-8'))

def translate_filename(filename, force_overwrite = False):
    filename_translation = os.path.join(LANGUAGE_DIR_PREFIX, language_code, filename)
    if os.path.isfile(filename_translation) and not force_overwrite:
        print("Existing translation found for {0}".format(filename))
        return 0
    print("Translating {0}".format(filename))
    mkdir_p(os.path.dirname(filename_translation))
    # artificial one-element array
    file_as_array = [get_file_as_text(filename)]
    try:
        all_translations = translate_array(file_as_array, language_code)
    except Exception as e:
        print("Exception during translation:", e)
        return 0
    write_array_as_file(all_translations, filename_translation)
    return 1


if __name__ == '__main__':

    language_code = args.language_code if args.language_code else DEFAULT_LANGUAGE_CODE

    # When passing the path explicitly - translate it only
    if args.input_path:
        translate_filename(args.input_path)
        sys.exit(0)

    # Otherwise attempt to translate up to `threshold` files
    translated_files_counter = 0
    threshold = args.threshold if args.threshold else DEFAULT_THRESHOLD

    for path, subdirs, files in os.walk("./docs/"):
        if translated_files_counter > threshold: continue
        for name in files:
            # exclude `images` directories, only treat the *.md files
            if file.endswith(".md"):
                filename = os.path.join(path, name)
                increment = translate_filename(filename)
                translated_files_counter += increment
                if translated_files_counter > threshold: continue
