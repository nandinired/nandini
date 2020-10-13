#!/bin/bash
curl https://api.github.com/repos/nandinired/nandini/pulls\?head\="nandinired:test" | grep labels/develop
rtn=$?
    if [ $rtn = 0 ]; then
        ls
        pwd
        pip install dirsync
        cp -p -r --backup=numbered `find ~/ -name dirsync -a -type d` ./
        cd .. && mkdir temp && cd temp && mv nandini/buildspec.yml ./
        cd nandini
        zip -qr source.zip ./ --exclude=buildspec.yml/
        aws s3 cp source.zip s3://test-buildartifactsbucket/source.zip
        #aws lambda update-function-code --function-name test --s3-bucket test-buildartifactsbucket --s3-key source.zip
        mv ../temp/buildspec.yml nandini
        sleep 3
        #aws s3 rm s3://test-buildartifactsbucket/ --recursive
    else
    echo "no label found"
    fi
echo "build successful"
echo "build complete"
