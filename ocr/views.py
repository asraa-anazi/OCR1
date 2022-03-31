
from multiprocessing import context
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from pdf2image import convert_from_path
from PIL import Image
import pyocr
import pyocr.builders 
import os 
from .scan import File

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')



def upload(request):
	
	if request.method == 'POST':
		u_file = request.FILES['uploadFile']
		fs = FileSystemStorage() 

		fn = fs.save(u_file.name, u_file) 
		scan = File(request.POST, request.FILES)
		if scan.is_valid():
			scan.save()
			return redirect('upload')

	else :
		scan = File		
	return render(request, 'upload.html', {
	 	'form': scan,

	})



 
'''''
def simple_upload(request):
	
		
		
		uploaded_file_url = fs.url(filename)
		return render(request, 'core/index.html', {
		'uploaded_file_url' : uploaded_file_url
		}
		)
		
	return render(request, 'core/index.html')
'''''