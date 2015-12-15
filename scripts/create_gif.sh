#!/bin/bash
# Derived from https://gist.github.com/tskaggs/6394639
# Requires:
#   imagemagick, ffmpeg

SCREENCAST=$1
GIF_FILE=$2
TIMESTAMP=$(date +'%s')
TMP_DIR="./png_${TIMESTAMP}"

# Trim the video if necessary
ffmpeg -i $SCREENCAST -ss 00:00:12.0 -c copy -t 00:00:7.0 ${TIMESTAMP}_${SCREENCAST}

# Create images from video
mkdir $TMP_DIR
ffmpeg -i ${TIMESTAMP}_${SCREENCAST} -vf scale=1280:-1 -r 10 ${TMP_DIR}/ffout%3d.png

# Convert images to gif
convert -delay 4 -loop 0 $TMP_DIR/ffout*.png $GIF_FILE

# Clean up
rm ${TIMESTAMP}_${SCREENCAST}
rm -rf $TMP_DIR
