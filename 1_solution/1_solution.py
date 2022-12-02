import cv2
import pytesseract
import modules
import os
from Levenshtein import distance
from numpy import mean

target = ['ТРАМП ДОНАЛЬД ДЖОН',
'ХАЛАБУДИНА ЮЛИЯ АЛЕКСЕЕВНА',
'ШАПОШНИКОВА ВИКТОРИЯ НИКОЛАЕВНА', 
'ДАЙМОНД ДМИТРИЙ АЛЕКСЕЕВИЧ', 
'СОКОЛОВ АНДРЕЙ АНДРЕЕВИЧ',
'МАКАРОВ РОМАН ЮРЬЕВИЧ',
'ВАСЛЕВСКИЙ ГРИГОРИЙ ПЕТРОВИЧ',
'ИМЯРЕК ЕВГЕНИЙ АЛЕКСАНДРОВИЧ',
'КУЗЕВАНОВ АЛЕКСАНДР ИГОРЕВИЧ',
'ЮМАКАЕВА ЖАННА АНАТОЛЬЕВНА',]

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tessdata_dir_config = r'--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

m_dist_list = []
print ('')
photos = os.listdir('../DataForOCR')

for i, photo in enumerate(os.listdir('../DataForOCR')):

    img = cv2.imread('..\\DataForOCR\\' + photo)
    img = img[int (img.shape[0]/2) : img.shape[0], 0 : img.shape[1]]

    data = pytesseract.image_to_string(img, lang='rus', config=tessdata_dir_config)
    names = modules.return_all_names(data)

    dist = distance(names, target[i])
    m_dist_list.append(dist)

    print ('for ' + photo + ' name is - ' + names + ' lev. distance is ' + str (dist))



print ('\nmean lev. distance is ' + str(mean(dist)))