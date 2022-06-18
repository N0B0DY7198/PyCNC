clear
echo [PyCNC] Setting up server!
apt-get update
apt-get install python3-pip
apt-get install screen
pip3 install requests
pip3 install psutil
pip3 install pystyle
echo [PyCNC] Finished setting up server!
sleep 2
clear
chmod +x CNC
cat readme.txt
echo Starting in 10 sec...
sleep 10
echo Any missing modules install them with 'pip3 install [module]'
clear
echo connect like this: IP: [server ip] PORT: Your choice TYPE: RAW
sleep 4
screen ./CNC
