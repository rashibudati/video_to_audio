#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:40:28 2020

@author: rashi
"""    
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
#success = 1
count = 0
list_text = []
while count!=14:
    text = ocr_core('C:/Users/BUD3KOR/Downloads/video_text/filesss/v_frames/%d.jpg' % count)
    text = text.replace('\n', ' ')
    count = count+1
    list_text.append(text)
    print(count)
print(list_text)
with open('C:/Users/BUD3KOR/Downloads/video_text/filesss/text.txt','w') as f:
    f.write(str(list_text))
    
