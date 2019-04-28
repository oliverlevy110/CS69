#!/bin/bash

systemctl stop network-manager 

iwconfig wlx000f004e07f7 essid "turtle19"

dhclient -r wlx000f004e07f7 
dhclient -v wlx000f004e07f7 

