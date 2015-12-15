mkdir tmp
cd tmp
wget http://docs.exabyte.io:81/files/public-documentation-gif.tar.gz
tar -xzvf public-documentation-gif.tar.gz
mv *.gif ../../docs/tutorials/images
cd -
rm -rf tmp
