#!/bin/bash

cd "$(dirname "$0")"

echo -e "\033[32We suggest you run script/pull_latest.sh to update project(not force), in case of some critical problems were fixed\033[0m"

sleep 1

echo -e "\033[32mActivating virtual environment...\033[0m"

python3 -m pip install virtualenv

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt



if [ $? -ne 0 ]; then
    echo -e "\033[31mFailed to activate virtual environment.\033[0m"
    exit 1
fi

echo -e "\033[32mVirtual environment activated successfully!\033[0m"

sleep 0.5
# Now run your Python script
python src/main.py