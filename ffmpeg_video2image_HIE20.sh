#!/bin/bash
VIDFOLDER=/Users/cycyang/Projects/ICME2021/HIE20/videos/
IMGFOLDER=/Users/cycyang/Projects/ICME2021/HIE20/images/

mkdir -p $IMGFOLDER

for filepath in ${VIDFOLDER}*; do
    echo $filepath
	filename=${filepath##*/}
	echo $filename
	basename=${filename%.*}
	extname=${filename#*.}
	echo $basename
	echo $extname
	subimgfolder="${IMGFOLDER}${basename}"
	echo $subimgfolder
	mkdir -p "${IMGFOLDER}${basename}"
	ffmpeg -i $filepath -start_number 0 -vsync 0 "${subimgfolder}/%06d.jpg"	
done
