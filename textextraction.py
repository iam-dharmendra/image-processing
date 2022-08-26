from cgi import print_environ_usage
from concurrent.futures import process
import csv
from dataclasses import replace
from datetime import datetime, timedelta
from unicodedata import name
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from PyPDF2 import PdfFileMerger, PdfFileReader
import requests
from django.conf import settings
# Create your views here.
from django.views.generic import View,TemplateView
import typing,re
from PIL import Image
from decimal import Decimal
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction
from borb.toolkit.location.location_filter import LocationFilter
from borb.pdf.canvas.geometry.rectangle import Rectangle
from borb.toolkit.text.regular_expression_text_extraction import RegularExpressionTextExtraction, PDFMatch
from word2number import w2n
from PyPDF2 import PdfFileReader
import PyPDF2 
import camelot,ocrmypdf
from pdf2image import convert_from_path



import cv2
import numpy as np
from pdfrw import PdfReader
images = convert_from_path('/home/user/Pictures/invoices/Accounting Voucher-2.pdf',dpi=250)
for image in images:
    image.save('avoutput.png')
img_for_box_extraction_path='avoutput.png'
img = cv2.imread(img_for_box_extraction_path, 0)
(thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
img_bin = ~img_bin
bw = cv2.adaptiveThreshold(img_bin, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                            cv2.THRESH_BINARY, 15, -2)
horizontal = np.copy(bw)
vertical = np.copy(bw)
cols = horizontal.shape[1]
horizontal_size = int(cols)
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
horizontalStructure1 = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
horizontal = cv2.erode(horizontal, horizontalStructure)
horizontal = cv2.dilate(horizontal, horizontalStructure1)
rows = vertical.shape[0]
verticalsize = int(rows)
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1,verticalsize))
verticalStructure1 = cv2.getStructuringElement(cv2.MORPH_RECT, (1,verticalsize))
vertical = cv2.erode(vertical, verticalStructure)
vertical = cv2.dilate(vertical, verticalStructure1)
verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 17))
hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 1))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=5)
verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=8)
img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=7)
res = verticle_lines_img + horizontal_lines_img
exp = img_bin - res
exp = ~exp
cv2.imwrite("avfinal.png",exp)
image1 = Image.open(r'avfinal.png')
im1 = image1.convert('RGB')
im1.save(r'avdifferent.pdf')

def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path,skip_text=True)
ocr('avdifferent.pdf','avfinal11.pdf')
b: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Buyer")
b1: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Bill to")
l: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Code")
m: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Invoice No.")
n: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Dated")
u: RegularExpressionTextExtraction = RegularExpressionTextExtraction("SGST")
f: RegularExpressionTextExtraction = RegularExpressionTextExtraction("CGST")
# u1: RegularExpressionTextExtraction = RegularExpressionTextExtraction("CENTRAL TAX (CGST)")
central: RegularExpressionTextExtraction = RegularExpressionTextExtraction("CENTRAL ")
integrated1: RegularExpressionTextExtraction = RegularExpressionTextExtraction("IGST")
integrated2: RegularExpressionTextExtraction = RegularExpressionTextExtraction("INTEGRATED ")
rup: RegularExpressionTextExtraction = RegularExpressionTextExtraction("Amount Chargeable ")
state: RegularExpressionTextExtraction = RegularExpressionTextExtraction("State Name")
gstnum: RegularExpressionTextExtraction = RegularExpressionTextExtraction("GSTIN/UIN")
main_dict = {}
main_file=open("avfinal11.pdf", "rb")

# try:
#     if b:
#         name = ''
#         d = PDF.loads(main_file, [b])
#         assert d is not None
#         matches: typing.List[PDFMatch] = b.get_matches_for_page(0)
#         assert len(matches) >= 0
        
#         if len(matches)>1:
            
        
#             data=matches[0].get_bounding_boxes()[0]
        
#             r: Rectangle = Rectangle(data.get_x() - Decimal(100),
#                                         data.get_y() - Decimal(82),
#                                         Decimal(700),
#                                         Decimal(50))
#             l0: LocationFilter = LocationFilter(r)
#             l1: SimpleTextExtraction = SimpleTextExtraction()
#             l0.add_listener(l1)
#             d = PDF.loads(main_file, [l0])
#             assert d is not None
#             y=l1.get_text_for_page(0)
#             if y:
#                 name = y        
#             else:
#                 data=matches[1].get_bounding_boxes()[0]
        
#                 r: Rectangle = Rectangle(data.get_x() - Decimal(100),
#                                             data.get_y() - Decimal(52),
#                                             Decimal(700),
#                                             Decimal(50))
#                 l0: LocationFilter = LocationFilter(r)
#                 l1: SimpleTextExtraction = SimpleTextExtraction()
#                 l0.add_listener(l1)
#                 d = PDF.loads(main_file, [l0])
#                 assert d is not None
#                 y=l1.get_text_for_page(0)  
#                 name = y
#         else:
    
#             data=matches[0].get_bounding_boxes()[0]
        
#             r: Rectangle = Rectangle(data.get_x() - Decimal(100),
#                                         data.get_y() - Decimal(52),
#                                         Decimal(700),
#                                         Decimal(50))
#             l0: LocationFilter = LocationFilter(r)
#             l1: SimpleTextExtraction = SimpleTextExtraction()
#             l0.add_listener(l1)
#             d = PDF.loads(main_file, [l0])
#             assert d is not None
#             y=l1.get_text_for_page(0)
#             name = y
#         main_dict['Buyer']=name
# except:
#     pass


# try:
#     if b1:
        
#         d = PDF.loads(main_file, [b1])
#         assert d is not None
#         matches: typing.List[PDFMatch] = b1.get_matches_for_page(0)
#         assert len(matches) >= 0
#         data=matches[0].get_bounding_boxes()[0]
#         r: Rectangle = Rectangle(data.get_x() - Decimal(100),
#                                     data.get_y() - Decimal(52),
#                                     Decimal(700),
#                                     Decimal(50))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)
#         d = PDF.loads(main_file, [l0])
#         assert d is not None
#         y=l1.get_text_for_page(0)
    
    
#         main_dict['Buyer']=y
    

    
# except:

#     pass
try:
    if l:
        d = PDF.loads(main_file, [l])
        assert d is not None
        matches: typing.List[PDFMatch] = l.get_matches_for_page(0)
        assert len(matches) >= 0
        data=matches[0].get_bounding_boxes()[0]
        r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                    data.get_y() - Decimal(30),
                                    Decimal(200),
                                    Decimal(40))
        l0: LocationFilter = LocationFilter(r)
        l1: SimpleTextExtraction = SimpleTextExtraction()
        l0.add_listener(l1)
        d = PDF.loads(main_file, [l0])
        assert d is not None
        y=l1.get_text_for_page(0)
        xyz = re.findall('\\d+',y)
    
    main_dict['State Code']=xyz[0]

except:
    pass
# try:
#     if m:
    
#         d = PDF.loads(main_file, [m])
#         assert d is not None
#         matches: typing.List[PDFMatch] = m.get_matches_for_page(0)
#         assert len(matches) >= 0
#         data=matches[0].get_bounding_boxes()[0]
        
#         r: Rectangle = Rectangle(data.get_x() - Decimal(10),
#                                 data.get_y() - Decimal(60),
#                                 Decimal(200),
#                                 Decimal(60))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)

#         d = PDF.loads(main_file, [l0])
#         assert d is not None
#         y=l1.get_text_for_page(0)
        
#         y1 = y.replace('\n','')
#     main_dict['Invoice Number']=y1.replace('Invoice No.' , '')
# except:
#     pass
# try:
#     if n:
#         d = PDF.loads(main_file, [n])
#         assert d is not None
#         matches: typing.List[PDFMatch] = n.get_matches_for_page(0)
#         assert len(matches) >= 0
#         data=matches[0].get_bounding_boxes()[0]
#         r: Rectangle = Rectangle(data.get_x() - Decimal(10),
#                                 data.get_y() - Decimal(60),
#                                 Decimal(200),
#                                 Decimal(60))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)

#         d = PDF.loads(main_file, [l0])

#         assert d is not None
        
#         z=l1.get_text_for_page(0)
#         main_dict['Date']=z.replace('Dated', '')
# except:
#     pass

# try:
#     if u:
#         d = PDF.loads(main_file, [u])
#         assert d is not None
#         matches: typing.List[PDFMatch] = u.get_matches_for_page(0)
#         assert len(matches) >= 0
#         data=matches[0].get_bounding_boxes()[0]
#         r: Rectangle = Rectangle(data.get_x() - Decimal(-700),
#                             data.get_y() - Decimal(30),
#                             Decimal(1200),
#                             Decimal(50))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)

#         d = PDF.loads(main_file, [l0])

#         assert d is not None
#         r = l1.get_text_for_page(0)     
    
#         sb = r.replace('SGST' , '').replace("%",'').replace(',','')
    
#         main_dict['SGST']=sb
#         main_dict['CGST']=sb
        

# except:
#     pass

# try:
#     if rup:
        
#         d = PDF.loads(main_file, [rup])
#         assert d is not None
#         matches: typing.List[PDFMatch] = rup.get_matches_for_page(0)
#         assert len(matches) >= 0
        
#         data=matches[0].get_bounding_boxes()[0]
#         r: Rectangle = Rectangle(data.get_x() - Decimal(130),
#                             data.get_y() - Decimal(80),
#                             Decimal(2000),
#                             Decimal(50))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)

#         d = PDF.loads(main_file, [l0])

#         assert d is not None
#         r = l1.get_text_for_page(0)    
#         num = w2n.word_to_num(r)
    
#         main_dict['Total']=num
    

# except:
#     pass


# if 'CGST' not in main_dict:
    
#     try:
#         if central:
            
#             assert d is not None
#             matches: typing.List[PDFMatch] = central.get_matches_for_page(0)
#             assert len(matches) >= 0
        
#             data=matches[0].get_bounding_boxes()[0]
#             r: Rectangle = Rectangle(data.get_x() - Decimal(-700),
#                                 data.get_y() - Decimal(50),
#                                 Decimal(1000),
#                                 Decimal(100))
#             l0: LocationFilter = LocationFilter(r)
#             l1: SimpleTextExtraction = SimpleTextExtraction()
#             l0.add_listener(l1)
#             d = PDF.loads(main_file, [l0])
#             assert d is not None
#             r = l1.get_text_for_page(0)     
        
#             main_dict['CGST']=r

#     except:
#         pass

#     try:
#         if integrated1:
        
#             d = PDF.loads(main_file, [integrated1])
#             assert d is not None
#             matches: typing.List[PDFMatch] = integrated1.get_matches_for_page(0)
#             assert len(matches) >= 0
        
#             data=matches[0].get_bounding_boxes()[0]
#             r: Rectangle = Rectangle(data.get_x() - Decimal(-700),
#                                 data.get_y() - Decimal(50),
#                                 Decimal(1000),
#                                 Decimal(100))
#             l0: LocationFilter = LocationFilter(r)
#             l1: SimpleTextExtraction = SimpleTextExtraction()
#             l0.add_listener(l1)
#             d = PDF.loads(main_file, [l0])
#             assert d is not None
#             r = l1.get_text_for_page(0) 
                
#             main_dict['IGST']=r             
#     except:
#         pass
# try:
#     if integrated2:
    
#         d = PDF.loads(main_file, [integrated2])
#         assert d is not None
#         matches: typing.List[PDFMatch] = integrated2.get_matches_for_page(0)
#         assert len(matches) >= 0
    
#         data=matches[0].get_bounding_boxes()[0]
#         r: Rectangle = Rectangle(data.get_x() - Decimal(-1350),
#                             data.get_y() - Decimal(40),
#                             Decimal(150),
#                             Decimal(50))
#         l0: LocationFilter = LocationFilter(r)
#         l1: SimpleTextExtraction = SimpleTextExtraction()
#         l0.add_listener(l1)
#         d = PDF.loads(main_file, [l0])
#         assert d is not None
#         r = l1.get_text_for_page(0)       
#         main_dict['IGST']=r  

# except:
#     pass  
try:
    if state:
        d = PDF.loads(main_file, [state])
        assert d is not None
        matches: typing.List[PDFMatch] = state.get_matches_for_page(0)
        assert len(matches) >= 0
    
        data=matches[1].get_bounding_boxes()[0]
        r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                data.get_y() - Decimal(10),
                                Decimal(400),
                                Decimal(20))
        l0: LocationFilter = LocationFilter(r)
        l1: SimpleTextExtraction = SimpleTextExtraction()
        l0.add_listener(l1)
        d = PDF.loads(main_file, [l0])
        assert d is not None
        r = l1.get_text_for_page(0)      
        before_keyword, keyword, after_keyword = r.partition(':')
        before_keyword, keyword, after_keyword = after_keyword.partition(',')
        main_dict['state']=before_keyword
except:
    pass  
try:
    if gstnum:
        d = PDF.loads(main_file, [gstnum])
        assert d is not None
        matches: typing.List[PDFMatch] = gstnum.get_matches_for_page(0)
        assert len(matches) >= 0
    
        data=matches[1].get_bounding_boxes()[0]
        r: Rectangle = Rectangle(data.get_x() - Decimal(10),
                                data.get_y() - Decimal(10),
                                Decimal(720),
                                Decimal(20))
        l0: LocationFilter = LocationFilter(r)
        l1: SimpleTextExtraction = SimpleTextExtraction()
        l0.add_listener(l1)
        d = PDF.loads(main_file, [l0])
        assert d is not None
        r = l1.get_text_for_page(0)      
        before_keyword, keyword, after_keyword = r.partition(':')
        main_dict['GSTnumber']=after_keyword
except:
    pass  
print(main_dict)