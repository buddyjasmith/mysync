#!/bin/bash

OSTYPE="$(uname -s)"
echo "$OSTYPE"
if [[ "$OSTYPE" == "Linux" ]]; then
    source lin_install.sh
    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Mac"
elif [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Lame"
fi