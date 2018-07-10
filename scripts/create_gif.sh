#!/bin/bash
# Derived from https://gist.github.com/tskaggs/6394639
# Requires:
#   imagemagick, ffmpeg
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
ffmpeg -i $INPUT -ss ${BEGIN} -c copy -t ${DURATION} ${TIMESTAMP}_$(basename $INPUT)

# Create images from video
mkdir $TMP_DIR

# -r  stands for FPS value
#    for better quality choose bigger number
#    adjust the value with the -delay in 2nd step
#    to keep the same animation speed
ffmpeg -i ${TIMESTAMP}_$(basename $INPUT) -vf scale=720:-1 -r 2 -vcodec ppm ${TMP_DIR}/ffout%3d.png

# Convert images to gif
# -delay 20 for example means the time between each frame is 0.2 seconds
#   When choosing this value
#       1 = 100 fps
#       2 = 50 fps
#       4 = 25 fps
#       5 = 20 fps
#       10 = 10 fps
#       20 = 5 fps
#       25 = 4 fps
#       50 = 2 fps
#       100 = 1 fps
#       in general 100/delay = fps
convert -delay 25 -loop 0  -layers optimize $TMP_DIR/ffout*.png +map +dither ${GIF}

# Optimize gif size; 256 colors are needed to remove grey shadows from background of GIF
convert -colors 256 ${GIF} ${GIF}
convert -layers remove-zero ${GIF} ${GIF}

# Clean up
rm ${TIMESTAMP}_$(basename $INPUT)
rm -rf $TMP_DIR
