#!/bin/bash
curl https://api.github.com/repos/nandinired/nandini/pulls{/number}
curl https://api.github.com/repos/nandinired/nandini/pulls\?base\="nandinired:dev" 
#curl https://api.github.com/repos/nandinired/nandini/pulls\?base\="nandinired:test" | grep labels/develop
rtn=$?
    if [ $rtn = 0 ]; then
        ls
        pwd
        pip install dirsync
        cp -p -r --backup=numbered `find ~/ -name dirsync -a -type d` ./
        mkdir ../temp 
        mv *.yml script.sh ../temp
        #zip -qr source.zip ./
        aws s3 cp . s3://test-buildartifactsbucket/source.zip
        #aws lambda update-function-code --function-name test1 --s3-bucket test-buildartifactsbucket --s3-key source.zip
        sleep 3
        #aws s3 rm s3://test-buildartifactsbucket/ --recursive
    else
    echo "no label found"
    fi
echo "build successful"
echo "build complete"
