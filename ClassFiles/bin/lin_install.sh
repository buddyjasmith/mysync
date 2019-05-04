#!/bin/bash
echo "The needed dependencies will be installed for MySync."
sudo apt update
if command -v sshfs &>/dev/null;then
    echo -e "\n"
else
    sudo apt install sshfs -y
fi

if command -v python3-pyqt5 &>/dev/null;then
    echo -e "\n"
else 
    sudo apt install python3-pyqt5
fi

if command -v python3 &>/dev/null; then
    echo -e "\n"
else
    sudo apt install python3
fi

if command -v python3-pip &>/dev/null;then
    echo -e "\n"
else    
    sudo apt install python3-pip
fi

