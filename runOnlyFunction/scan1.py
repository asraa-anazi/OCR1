from pdf2image import convert_from_path
from PIL import Image
import pyocr
import pyocr.builders 
import os 
import re

RBS = ['RBS', 'Random Blood Suger', 'Random Blood Glucose', 'Plasma Glucose Random', 'RANDOM GLUCOSE']
FBS = ['FBS', 'Fasting Blood Suger', 'Fasting Blood Glucose', 'Plasma Glucose Fasting', 'FASTING GLUCOSE']

def get_fasting_glucos(pdf_file_name, keyword):
    pages = convert_from_path(pdf_file_name, 200)


    filename = 'temp.jpg'
    pages[0].save(filename, 'JPEG')
    tool = pyocr.get_available_tools()[0]
    img = Image.open(filename)

    txt = tool.image_to_string(
    img,
    lang='eng',
    builder=pyocr.builders.TextBuilder()
    ).lower()

    keyword = keyword.lower()

    res = re.search(keyword, txt)
    for line in txt.splitlines():
        res = re.search(keyword, line)
        if res:
            res=line
            break

    os.remove(filename)
    return re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", res)[0].strip()

print (get_fasting_glucos('m.pdf', 'Plasma Glucose Fasting'))
