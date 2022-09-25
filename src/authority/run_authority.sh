#!/bin/bash -x
node app.js &
sleep 5
python3 -u client.py 

sleep 600
exit
