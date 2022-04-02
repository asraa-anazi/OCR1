from PIL import Image as img  
import pytesseract as PT  
import sys, re
from pdf2image import convert_from_path as CFP  
import os, cgi


#import cgitb; cgitb.enable()


#form = cgi.FieldStorage()
# Get filename here.

PDF_file_1 = '4d9c37dc.pdf'

pages_1 = CFP(PDF_file_1, 150)  

image_counter1 = 1  

for page in pages_1:  
    

    filename1 = "Page_no_" + str(image_counter1) + " .jpg"  
    page.save(filename1, 'JPEG')  
    image_counter1 = image_counter1 + 1  
    
filelimit1 = image_counter1 - 1  
    
out_file1 = "output_text.txt"  
f_1 = open(out_file1, "a")  


patterns = ['GLUCOSE', 'Glucose', 'RBS', 'FBS', 'glucose']
for K in range(1, filelimit1 +1 ):  
    
    
    filename1 = "Page_no_" + str(K) + " .jpg" 
    
    text1 = PT.image_to_string (img.open (filename1)) 
    
    #pattern = re.compile("GLUCOSE")
    #for line in open(out_file1):
        #for match in re.finditer(pattern, line):

    for pattern in patterns:
        if re.search(pattern, text1):
            if re.match('GLUCOSE', pattern):
                m = re.findall(r"GLUCOSE (.*)" , text1)
                x = re.search(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str(m))
                print(x.group(0))

            elif re.match('Glucose', pattern):
                m = re.findall(r"Glucose (.*)" , text1)
                x = re.search(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str(m))
                print(x.group(0))

            elif re.match('RBS', pattern):
                m = re.findall(r"RBS (.*)" , text1)
                x = re.search(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str(m))
                print(x.group(0))

            elif re.match('FBS', pattern):
                m = re.findall(r"FBS (.*)" , text1)
                x = re.search(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str(m))
                print(x.group(0))

            elif re.match('glucose', pattern):
                m = re.findall(r"glucose (.*)" , text1)
                x = re.search(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", str(m))
                print(x.group(0))

        else: 
            print ("None")
            break
    
    
f_1.close()  