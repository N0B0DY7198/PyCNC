@echo off
type readme.txt
echo connect IP: 127.0.0.1 PORT What ever one you chose TYPE raw
echo starting soon!
ping 1.1.1.1 -n 10 >nul
python main.py
pause>nul
