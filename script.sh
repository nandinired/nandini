#!/bin/bash
#curl https://api.github.com/repos/nandinired/nandini/pulls | grep labels > output
#curl https://api.github.com/repos/nandinired/nandini/pulls | grep labels/test
curl https://api.github.com/repos/nandinired/nandini/pulls | grep nandinired:test
rtn=$?
if [ $rtn = 0 ]; then
#for var in $label;do
    curl https://api.github.com/repos/nandinired/nandini/pulls | grep labels/develop
    rtn=$?
    if [ $rtn = 0 ]; then
        ls
        pwd
        pip install dirsync
        cp -p -r --backup=numbered `find ~/ -name dirsync -a -type d` ./
        #ls
        #zip -qr source.zip ./
        #aws s3 cp source.zip s3://test-buildartifactsbucket/source.zip
        #aws lambda update-function-code --function-name test --s3-bucket test-buildartifactsbucket --s3-key source.zip
        sleep 3
        #aws s3 rm s3://test-buildartifactsbucket/ --recursive
        break
    fi
    echo "no label found"
fi
echo "pull request is not created for test branch"
done
