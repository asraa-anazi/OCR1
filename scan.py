from PIL import Image as img  
import pytesseract as PT  
import sys, re
from pdf2image import convert_from_path as CFP  
import os, cgi


#import cgitb; cgitb.enable()


#form = cgi.FieldStorage()
# Get filename here.
RBS = ['RBS', 'Random Blood Suger', 'Random Blood Glucose', 'Plasma Glucose Random']
FBS = ['FBS', 'Fasting Blood Suger', 'Fasting Blood Glucose', 'Plasma Glucose Fasting']
PDF_file_1 = 'myopd-path-lab-BSL-converted.pdf'

pages_1 = CFP(PDF_file_1, 150)  

image_counter1 = 1  

for page in pages_1:  
    

    filename1 = "Page_no_" + str(image_counter1) + " .jpg"  
    page.save(filename1, 'JPEG')  
    image_counter1 = image_counter1 + 1  
    
filelimit1 = image_counter1 - 1  
    
out_file1 = "output_text.txt"  
f_1 = open(out_file1, "a")  
    
for K in range(1, filelimit1 +1 ):  
    
    filename1 = "Page_no_" + str(K) + " .jpg" 
    

    text1 = PT.image_to_string (img.open (filename1))
    #print(text1)
    
    
    m = re.findall(r"Glucose (\b\d+) " , text1)
    
    #m = text1.find('Plasma Glucose Fasting')
    x = re.sub("/(stackoverflow)/", "", str(m))

   

    print(m[0])
    print(x)
    #f_1.write(m[0])  
    
    
f_1.close()  