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
import re
from googleapiclient.discovery import build

# Top-level directory for multiple languages
LANGUAGE_DIR_PREFIX = 'lang'
DEFAULT_LANGUAGE_CODE = 'ja'
# Number of new files to translate / API requests.
# Total number of .md files in repo is ~500 as of 2019-02.
DEFAULT_THRESHOLD = 10
# Google API key to communicate with Cloud Translate API
# DO NOT COMMIT
GOOGLE_API_KEY = 'AIzaSyDPJoU9dIfMWTdXc-IFwcBuy4uboVwU5K0'

URL_REGEX = r'(\[[^\[\]]+\]\([^)]+\))'

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
        format="text",
        q=array
      ).execute()['translations']
    return list(map(lambda x: x['translatedText'], translations))

def write_array_as_file(array, filename, separator="\n"):
    with open(filename, "w+") as f1:
        f1.write(separator.join(array).encode('utf-8'))

def translate_filename(filename, force_overwrite = False):
    filename_translation = os.path.join(LANGUAGE_DIR_PREFIX, language_code, filename)
    if os.path.isfile(filename_translation) and not force_overwrite:
        print("Existing translation found for {0}".format(filename))
        return 0
    print("Translating {0}".format(filename))
    mkdir_p(os.path.dirname(filename_translation))
    # artificial one-element array
    file_text = get_file_as_text(filename)
    file_chunks = re.split(URL_REGEX, file_text, flags=re.MULTILINE)
    file_as_array = file_chunks
    # print(file_chunks)
    try:
        all_translations = translate_array(file_as_array, language_code)
        # print("".join(all_translations).encode('utf-8'))
    except Exception as e:
        print("Exception during translation:", e)
        return 0

    # replace all odd elements - "separators" by their original values
    for idx, val in enumerate(all_translations):
        if idx % 2 != 0:
            all_translations[idx] = file_chunks[idx]

    write_array_as_file(all_translations, filename_translation, "")
    return 1


if __name__ == '__main__':

    language_code = args.language_code if args.language_code else DEFAULT_LANGUAGE_CODE

    # When passing the path explicitly - translate it only
    if args.input_path:
        translate_filename(args.input_path)
        sys.exit(0)

    # Otherwise attempt to translate up to `threshold` files
    translated_files_counter = 0
    break_out_of_loop = False
    threshold = args.threshold if args.threshold else DEFAULT_THRESHOLD

    for path, subdirs, files in os.walk("./docs/"):
        if break_out_of_loop: continue
        for name in files:
            if break_out_of_loop: continue
            # exclude `images` directories, only treat the *.md files
            if name.endswith(".md"):
                filename = os.path.join(path, name)
                increment = translate_filename(filename)
                translated_files_counter += increment
                if translated_files_counter >= threshold:
                    break_out_of_loop = True
