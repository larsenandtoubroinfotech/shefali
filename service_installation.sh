#!/bin/bash
#service installation script is general script whatever service ypu want to install give its name while runnign the script that perticular service will gets installed on that instance
service_name=$1
apt-get update
apt-get install $service_name
service $service_name start
