#!/bin/bash
# Derived from https://gist.github.com/tskaggs/6394639
# Requires:
#   imagemagick, ffmpeg
# On OSX:
#   brew install imagemagick
#   brew install ffmpeg

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
    echo "create_gif.sh -i=INPUT -o=GIF -b=BEGIN(00:00:00.0) -d=DURATION(00:00:01.0) "
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
ffmpeg -i $INPUT -ss ${BEGIN} -c copy -t ${DURATION} ${TIMESTAMP}_${INPUT}

# Create images from video
mkdir $TMP_DIR
ffmpeg -i ${TIMESTAMP}_${INPUT} -vf scale=1280:-1 -r 10 ${TMP_DIR}/ffout%3d.png

# Convert images to gif
convert -delay 4 -loop 0 \
    -layers OptimizeTransparency \
    $TMP_DIR/ffout*.png ${GIF}

# Optimize gif size
gifsicle -O2 ${GIF} --colors 256 -o ${GIF}

# Clean up
rm ${TIMESTAMP}_${INPUT}
rm -rf $TMP_DIR
