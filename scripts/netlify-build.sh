git submodule update --recursive --init
git lfs install
git lfs pull
# git LFS objects can alternatively be handled via environmental variables
# GIT_LFS_ENABLED=true and GIT_LFS_FETCH_INCLUDE
# https://answers.netlify.com/t/problem-checking-out-file-stored-in-git-lfs-on-github/103897/7

# pip packages are automatically installed by netlify
# if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
mkdocs build
