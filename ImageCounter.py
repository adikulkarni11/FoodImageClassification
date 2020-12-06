# Aditya Kulkarni
# Python program to count the number of images collected.
# As each text file has the links of images spaced out to one result per line, I counted the number of lines in all the text files in the directory.  
# This was a quick way to count to images and number of folders as I wanted.

import os
import sys
import pathlib

fileNum = 0
imageCounter = 0

for path in pathlib.Path(r"PATH TO ZIP").iterdir():
    if path.is_file():
        fileNum += 1
        current_file = open(path, "r")
        #print(path)
        Content = current_file.read() 
        CoList = Content.split("\n") 
        for img_link in CoList: 
            if img_link:
                imageCounter += 1
        #print(current_file.read())
        current_file.close()

# Result tallied 19907 images in 487 folders
print(imageCounter, fileNum)


