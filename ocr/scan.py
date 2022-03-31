from PIL import Image as img  
import pytesseract as PT  
import sys, re
from pdf2image import convert_from_path as CFP  
import os, cgi
from django import forms
from .models import filename1


import cgitb; cgitb.enable()


class File(forms.ModelForm):
    class Meta:
        form = cgi.FieldStorage()
# Get filename here.
        PDF_file_1 = form['filen']  
        pages_1 = CFP(PDF_file_1, 100)  

        image_counter1 = 1  

        for page in pages_1:  
    

            filen = "Page_no_" + str(image_counter1) + " .jpg"  
            page.save(filen, 'JPEG')  
            image_counter1 = image_counter1 + 1  
    
        filelimit1 = image_counter1 - 1  
    
        out_file1 = "output_text.txt"  
        f_1 = open(out_file1, "a")  
    
        for K in range(1, filelimit1 + 1):  
    
            filename1 = "Page_no_" + str(K) + " .jpg"  

            text1 = PT.image_to_string (img.open (filename1))
    

            m = re.findall(r"FASTING GLUCOSE [\d\\.]+", text1)
            if m:
                print(m[0])
            w = re.findall(r"RANDOM GLUCOSE [\d\\.]+", text1)
            if w:
                print(w[0])
    
            f_1.close()  

