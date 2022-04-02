from pdf2image import convert_from_path, exceptions
from PIL import Image
import pyocr
import pyocr.builders 
import os 
import re


def find_word(line, keyword):
    RBS = ['RBS',
            'Random Blood Suger', 
            'Random Blood Glucose', 
            'Plasma Glucose Random',
            'Random Glucose', 
            ]

    FBS = ['FBS', 
    'Fasting Blood Suger', 
    'Fasting Blood Glucose', 
    'Plasma Glucose Fasting',
    'Fasting Glucose'
    ]
    list_of_words = FBS if keyword == "FBS" else RBS

    res = None
    for word in list_of_words:
        if word.lower() in line.lower():
            res = line
            break
    return res
        
 

def get_fasting_glucos(pdf_file_name, keyword):
    try:
        pages = convert_from_path(pdf_file_name, 150)
        filename = 'temp.jpg'
        pages[0].save(filename, 'JPEG')
        tool = pyocr.get_available_tools()[0]
        img = Image.open(filename)
        res = ''
        txt = tool.image_to_string(
        img,
        lang='eng',
        builder=pyocr.builders.TextBuilder()
        ).lower()
        for line in txt.splitlines():
            res = find_word(line, keyword=keyword)
            if res:
                break
            else:
                pass
        return re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", res)[0].strip()

    except exceptions.PDFPageCountError:
        print ("File not found")
    except Exception as e:
        print ("Thers something error in your pdf file please check !")
        




print (get_fasting_glucos('m.pdf', 'RBS'))
