#!/bin/bash

# ---------------------------------------------------------- #
#  Written @ Exabyte.io                                      #
#  Uploads images dir to a remote file server                #
#  Puts dir into /uploads folder                             #
# ---------------------------------------------------------- #

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

FILE_SERVER="http://files.exabyte.io"
FILE_DIR="uploads"

LOCAL_DIRNAME="${THIS_SCRIPT_DIR}/../lang/en/docs/images"
REMOTE_DIRNAME=""

cat > tmp.files.key <<EOF
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAoWB6FKycjPrSHau/RDR63tXnNvRYX4+++UYpUH/5FNnwmqHO
xR+vzR1NF4kptLNIE9OAQdsgCfNma7CBIhopWJcuoGaF45ggK3/13PQ2xKEIO03W
UDMOTQg5eF0AWdO8KPftB9BOqWLu1fjKfOsz0gEBNrFs8H4H3cQBzOkp+V67fg/F
0xe3M6StcWtNZ0D3tKenLG1CZ2t4ONBjwyF6CdfpKwltmOg+2MXqOMnDjLM4IsdT
Riy3eEQtSTDU8/ote5aF44XDw1xMgOCQVABGQHDubnq2amP2RQHUH6LhlrRzVDAz
6DJLHZMm+GAf84jy4ZIZpSI9ip9zINJGQoRSgwIDAQABAoIBAHZoissWqDvNYlTB
CzNpamqM+v1Ypmtf1tmiwHe/nqzNCPz9EvGSwXS4NjO5we9DyPQ7MRWhSc3jWVhV
BztVhNbq/xxUfZM0sQ4Z8vXv/yuhmJ+jCkiIXcrp6PlHDBXdBWfuGm6sSruAywwX
Y8Pq9Hf3osNVxkBjyTPQOR34S4Mb9AuRlf+h+p8J1m0aV9ylohgYUDyoBwmyUFMd
+p+cjDIE14KjMCNcQC1WOIYtNYRtCnQ+xZLl3aHCkPlYA4IZ53VhMg4x+Igr7Hi1
xJNgu7CqMZ6Gn09JNi5FP1JLg952iU+3AMcHjiW6iQHCoi/EZTcHJYvXNh18rNCp
ggJonHkCgYEA0DvHAkq+tNd9yI82HJkDk9VYBbVe0oFEIDJbwEDC1XdQN32Oj2en
R97hKZOZb1BZpBXhk+iG5MLzVY+aqOXo4u7VM+0obHygcTnI3KKLc6nCkvaWns0x
r1kL5VHeGyj4P1gyzWng3Yljpmgy7LD+i/S1/sEmaDZSppE5Kogc658CgYEAxmUb
wR1PUD1z//XPkSi2kxQwZRg6wibD70C4ww9BOEp8BDKRfqqnKn2FAGDYQXHwws0r
98b+7DoHY01BSWdgHxCAkN1sSpFiqlrhI1HFqZKkGjTvCIWauEwzMHaVY1w+pSoe
LlVuL4ZEDDZmXcG7IplMHL+j5Z21mtX/K6AG7p0CgYB3jCoXtcPA3Qp4r0d4qZw1
LkGHnXXf0pjDB0ZHnKZ+mS4zfWDwEaknCN0p2nQ3ROEB5BIKsW9oPEgpMfWvy7al
OkqqshgIGJCgEHWxvZvj/m0XpHwalWFV8wByWkryOtYyv7cC2Stg5HSSX7YEzySE
QyyNImSjZbSTrkIsmdJIrwKBgQCTHerk2y0zXT6lscwH4l7w1enFLaB01HY69o2L
58X/TgyEuFL30OhBM+7qhuYWMb3NVoOiK2hiF+3ejy04l3XJ01zjD6775K97kASf
QkYHJvyVimcutJQ00hyrdWP12DOEGqViymr4xuGzBKwIHl78mxy7vMh2vuoqNUIR
QYuiaQKBgQCofs5rSq4j+rID9pCMP9OLvWe0fsupdAFOYkwkkmG36xLgLssumsPs
F8dsC2R+1rlMdKRQ57lX6pBKl8qePWQJrfmtdt9m5QDgIrRXSfZVYfR+YA4k1mLG
OlyeUuvndmWnEZFTGA1sm+Ny1H+msqlweFOzaY2pT96bSwyE5RuZTA==
-----END RSA PRIVATE KEY-----
EOF

chmod 400 ./tmp.files.key

# Try scp and exit if it fails
# scp -r -i tmp.files.key ${LOCAL_DIRNAME} files@exabyte.io:${FILE_DIR}/${REMOTE_DIRNAME} || exit 1
rsync -avz --update --no-perms --no-owner --no-group \
    -e "ssh -i tmp.files.key -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" \
    --progress ${LOCAL_DIRNAME} files@exabyte.io:${FILE_DIR}/${REMOTE_DIRNAME}/

rm -f tmp.files.key*

echo "Images uploaded successfully to ${FILE_SERVER}:18/${FILE_DIR}"
