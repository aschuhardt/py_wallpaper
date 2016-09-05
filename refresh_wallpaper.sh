#!/bin/bash

while true; do
	#set filename of output image
	filename="/home/aschuhardt/cur_wallpaper.png"

	#if the file exists, then delete it
	if [ -e $filename ]
	then
		rm $filename
	fi

	#run the script to generate a new image
	/bin/python3.5 /home/aschuhardt/py_wallpaper/wallpaper_maker.py $filename 1366 768 64 6 7 

	#set the new image as wallpaper
	feh --bg-center $filename

	#wait 5 minutes before looping
	sleep 5m
done
