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
TIMESTAMP=tmp #$(date +'%s')
TMP_FILE=${TIMESTAMP}_$(basename ${INPUT})
TMP_DIR="${THIS_SCRIPT_DIR}/png_${TIMESTAMP}"

# Trim the video
ffmpeg -i ${INPUT} -ss ${BEGIN} -c copy -t ${DURATION} ${TIMESTAMP}_$(basename ${INPUT})

# Create images from video
mkdir ${TMP_DIR}
#  -r option affects per-second frame resolution
ffmpeg -i ${TMP_FILE} -vf scale=960:-1 -r 10 ${TMP_DIR}/ffout_$(basename ${INPUT})_%3d.png

# # Convert images to gif
# # -delay option affects delay between subsequent frames (correlates with `-r` above)
# convert -monitor -delay 4 -loop 0 -layers optimize ${TMP_DIR}/ffout*.png +map +dither ${GIF}

# # Optimize gif size
# convert -colors 64 ${GIF} ${GIF}
# convert -layers remove-zero ${GIF} ${GIF}

# # Clean up
# rm ${TIMESTAMP}_$(basename ${INPUT})
# rm -rf ${TMP_DIR}
