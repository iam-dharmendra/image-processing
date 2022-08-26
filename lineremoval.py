from lib2to3.pytree import convert
from PIL import Image, ImageEnhance
import numpy as np
import random
import cv2
from numpy import ndim

# pil=Image.open('/home/user/Downloads/rose.jpg')
# # pil=pil.convert('L')
# pil=np.array(pil)
# pil=pil+100
# pil=Image.fromarray(pil)
# pil.show()

# pil_image = Image.fromarray((np.array((Image.open('/home/user5/Documents/ank10/Image Processing/test py/maybach.jpg')).convert("L"))) + 20).show()



# To read image from disk, we use
# cv2.imread function, in below method,

# img = cv2.imread("/home/user/Downloads/rose.jpg",1)
# img = cv2.imread("/home/user/Music/dharmendra/image_processing/images/LDII_042729_TB_00001_2.tif",1)
# dim=(900,700)

## for resizing the image and showing.
# img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# (thresh, img)=cv2.threshold(img,120,255,cv2.THRESH_BINARY)

# cv2.imshow('image',img)
# cv2.waitKey(100000)
# cv2.destroyAllWindows()

## opeartions with image array

## first method

# img=np.where(img>151,0,img)

# ## second method
# counter=0
# for i in img: 
#     counter1=0
#     for j in i:
#         counter2=0
#         for k in j:
#             if k>100:
#                 img[counter][counter1][counter2]=0
#             counter2+=1
#         counter1+=1
#     counter+=1            


# print(img.shape)
# print(img.dtype)


# cv2.imshow('image',img)
# cv2.waitKey(3600)
# cv2.destroyAllWindows()

# change  colour of image #
# img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


## for erode and dilate

# kernel = np.ones((3,3), np.uint8)
# img_dilation = cv2.dilate(img,kernel,iterations=1)
# img_erosion = cv2.erode(img,kernel,iterations=5)

# cv2.imshow('image',img_erosion)
# cv2.waitKey(3600)
# cv2.destroyAllWindows()

## for making outline of image

# img=cv2.Canny(img, 100, 200)

# Apply bilateral filter with 
# d = 15,

# sigmaColor = sigmaSpace = 75.
# bilateral = cv2.bilateralFilter(img, 45, 75, 75)

# cv2.imshow('image',img)
# cv2.waitKey(3600)
# cv2.destroyAllWindows()

# for saving image in any formate#

# cv2.imwrite('/home/user/Music/dharmendra/image_processing/image.tif',img)



import cv2
 
# Use the second argument or (flag value) zero
# that specifies the image is to be read in grayscale mode
img = cv2.imread('/home/user/Music/dharmendra/image_processing/images/LD2.jpg')
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
print(type(thresh1))
cv2.imshow('Grayscale Image', thresh1)
cv2.waitKey(100000)