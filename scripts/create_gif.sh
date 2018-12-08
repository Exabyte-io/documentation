#!/bin/bash
# Derived from:
#   https://gist.github.com/tskaggs/6394639,
#   https://askubuntu.com/questions/648603/how-to-create-an-animated-gif-from-mp4-video-via-command-line
# Requires:
#   imagemagick (~7.0.8_6), ffmpeg (3.4.2)
#   On OSX:
#       brew install imagemagick
#       brew install ffmpeg

get_script_dir () {
    SOURCE="${BASH_SOURCE[0]}"
    # While $SOURCE is a symlink, resolve it
    while [ -h "$SOURCE" ]; do
        DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
        SOURCE="$( readlink "$SOURCE" )"
        # If $SOURCE was a relative symlink (so no "/" as prefix,
        # need to resolve it relative to the symlink base directory
        [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
    done
    DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
    echo "$DIR"
}

THIS_SCRIPT_DIR=$(get_script_dir)

#
# Print usage
#
usage () {
    echo "create_gif.sh -i=INPUT -o=OUTPUT -b=00:00:00.0 -d=00:00:01.0"
    exit 1
}

#
# Check arguments passed to the script
#
#   Args:
#       $@: all arguments passed to the script
#
check_args () {
    if [ $# -eq 0 ]; then usage; fi
    # set default
    BEGIN="00:00:00.0"
    DURATION="00:00:01.0"
    for i in "$@"
    do
        echo $i
        case $i in
            -i=*|--input=*)
                INPUT="${i#*=}"
                shift
            ;;
            -o=*|--output=*)
                GIF="${i#*=}"
                shift
            ;;
            -b=*|--restore-db=*)
                BEGIN="${i#*=}"
                shift
            ;;
            -d=*|--options=*)
                DURATION="${i#*=}"
                shift
            ;;
            *)
                usage
            ;;
        esac
    done
}

#
check_args $@

# Set variables
TIMESTAMP=$(date +'%s')
TMP_DIR="${THIS_SCRIPT_DIR}/png_${TIMESTAMP}"

# Trim the video
ffmpeg -i $INPUT -ss ${BEGIN} -t ${DURATION} ${TIMESTAMP}_$(basename $INPUT)

# Crop out dark black sides
# ffmpeg -i $INPUT -filter:v "crop=1724:1080:98:0" ${TIMESTAMP}_$(basename $INPUT)

mkdir $TMP_DIR

# Create images from video
#   -r stands for frame per second (FPS) value. For better quality choose bigger number.
#   Adjust the value with the `-delay` option below to keep the same animation speed.
ffmpeg -i ${TIMESTAMP}_$(basename $INPUT) -vf scale=720:-1 -r 5 -vcodec ppm ${TMP_DIR}/ffout%3d.png

# Convert images to gif
#   `-delay 20` below means the time between each frame is 0.2 seconds
#   When choosing this value 100/delay = fps: 1 = 100 fps, 50 = 2 fps, 100 = 1 fps.
#   When the FPS used by ffmpeg is lower than the equivalent FPS below the resulting video is speed up and vice versa.
convert -delay 20 -loop 0 -layers optimize $TMP_DIR/ffout*.png +map +dither ${GIF}

# Optimize gif size; 256 colors are needed to remove grey shadows from background of GIF
convert -colors 256 ${GIF} ${GIF}
convert -layers remove-zero ${GIF} ${GIF}

# Clean up
rm ${TIMESTAMP}_$(basename $INPUT)
rm -rf $TMP_DIR
