# Simple python program to view multiple images as a collage.

import cv2
import numpy as np
#Read First Image
img1=cv2.imread('IMAGE 1')
#Read Second Image
img2=cv2.imread('IMAGE 2')

#Read Third Image
img3=cv2.imread('IMAGE 3')
#Read Fourth Image
img4=cv2.imread('IMAGE 4')


#concatanate image Horizontally
img_concate_Hori=np.concatenate((img1,img2),axis=1)

cv2.waitKey(0)
#cv2.destroyAllWindows()