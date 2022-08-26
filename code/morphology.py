import cv2
import numpy as np
from PIL import Image 

# load image
img = cv2.imread("zzest_bw_dpi.jpg")

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#noise removal
saltpep = cv2.fastNlMeansDenoising(gray,None,9,13)


# blur
blur = cv2.GaussianBlur(saltpep, (0,0), sigmaX=33, sigmaY=33)

# divide
divide = cv2.divide(gray, blur, scale=255)

# otsu threshold
#thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# apply morphology
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,2))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


# cv2.imwrite("hebrew_text_division_morph.jpg")

col = Image.open("hebrew_text_division_morph.jpg") #read image 


col.save("final12.jpg",dpi=(300,300))
# display it
cv2.imshow("gray", blur)
cv2.imshow("noise removal", saltpep)
cv2.imshow("divide", divide)
#cv2.imshow("thresh", thresh)
#cv2.imshow("morph", morph)
cv2.waitKey(0)
cv2.destroyAllWindows()