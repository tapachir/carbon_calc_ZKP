#!/bin/bash -x

node app.js &
sleep 30
python3 -u client.py

sleep 600
exit
