#!/bin/bash
#Set up the environment for the Networks Tutorial
#Released into the public domain (can be used by 
#anyone without limitation; you may delete the
#comments at the top)

PROGRAM=$(basename $0)

function die(){
local errmsg="$1" errcode="${2:-1}"
echo "ERROR: ${errmsg}"
exit ${errcode}
}

function check_installed(){

if hash ${1} 2>/dev/null
then
    echo "${1} is installed"
else
    die "${1} not installed" 1 
fi
}


#check the installation

to_check_install="pip virtualenv"

for prgrm in $to_check_install
do
    check_installed $prgrm
done


echo "Creating the virtualenv"
virtualenv -p $(which python3) --no-site-packages network-venv
source ./network-venv/bin/activate

echo "Installing dependencies"
pip install -r requirements.txt
pip install ./python-louvain/
