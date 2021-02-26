import sys
import os
from PIL import Image
import os.path

# Main directory that includes images. Can be a directory of directories.
directory = r''ENTER DIR NAME HERE'

for root, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith((".png")):  # I'm looking for all PNG Files in the main directory  
            #print(name)             # Ran only the print at the start, just making sure it works
            im = Image.open("ENTER MAIN DIR/ SUB DIR OF IMAGES HERE"+name) # Image files need to be present in specified dir here. My dir here was 'maindir/subdir'
            #print(name[:-4])
            jpgname = name[:-4]+".jpeg"
            #print(jpgname)
            im.save("DIR LOCATION WHERE YOU WANT TO SAVE FILES"+jpgname, "JPEG")
            os.remove(name)