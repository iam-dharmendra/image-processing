from PIL import Image 

size = 7016, 4961
im = Image.open("LDII_042729_JB_00001_1.jpg")
im_resized = im.resize(size, Image.ANTIALIAS)
im_resized.save("my_image_resized.png", "PNG")