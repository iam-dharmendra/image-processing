from PIL import Image 
import cv2
col = Image.open("LDII_042729_JB_00001_1.jpg") #read image 
gray = col.convert('L')  #conversion to gray scale 
saltpep = cv2.fastNlMeansDenoising(gray,None,9,13)
bw = saltpep.point(lambda x: 0 if x<205 else 255, '1') 

bw.save("zzzzest_bw_dpi.jpg",dpi=(300,300))