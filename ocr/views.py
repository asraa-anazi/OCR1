
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def simple_upload(request):
	if requst.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'core/index.html', {
		'uploaded_file_url' : uploaded_file_url
		}
		)
		
	return render(request, 'core/index.html')

from pdf2image import convert_from_path
from PIL import Image
import pyocr
import pyocr.builders 
import os 


def get_fasting_glucos(pdf_file_name, keyword):
    pages = convert_from_path(pdf_file_name, 500)


    filename = 'temp.jpg'
    pages[0].save(filename, 'JPEG')
    tool = pyocr.get_available_tools()[0]
    img = Image.open(filename)

    txt = tool.image_to_string(
    img,
    lang='eng',
    builder=pyocr.builders.TextBuilder()
    )
    res = ''
    for line in txt.splitlines():
        if keyword in line:
            res = line
            break
    os.remove(filename)
    return float(line.split(' ')[2])