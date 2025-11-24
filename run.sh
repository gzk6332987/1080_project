#!/bin/bash

echo -e "\033[32mActivating virtual environment...\033[0m"

source venv/bin/activate

if [ $? -ne 0 ]; then
    echo -e "\033[31mFailed to activate virtual environment.\033[0m"
    exit 1
fi

echo -e "\033[32mVirtual environment activated successfully!\033[0m"

sleep 0.5
# Now run your Python script
python src/main.py