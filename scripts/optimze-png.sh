#!/bin/bash
# Derived from http://www.clock.co.uk/blog/optimise-your-pngs-from-the-terminal-in-osx
# NOTE: This script will optimize the input png file and rewrites on the same file.
# Requires:
#   optipng
#   On OSX:
#       brew install optipng

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
    echo "optimize-png.sh [-o{2-7}] -i=image.png"
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
    OPTLEVEL="2"
    for i in "$@"
    do
        echo $i
        case $i in
            -i=*|--input=*)
                INPUT="${i#*=}"
                shift
            ;;
            -o=*|--optlevel=*)
                OPTLEVEL="${i#*=}"
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

# Optimize the input png
optipng -o${OPTLEVEL} $INPUT
