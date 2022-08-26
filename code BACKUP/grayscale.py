from PIL import Image 
import cv2
col = Image.open("LDII_042729_JB_00001_1.jpg") #read image 
gray = col.convert('L')  #conversion to gray scale 
bw = gray.point(lambda x: 0 if x<205 else 255, '1') 

bw.save("zzest_bw_dpi.jpg",dpi=(300,300))

image = cv2.imread("zzest_bw_dpi.jpg")