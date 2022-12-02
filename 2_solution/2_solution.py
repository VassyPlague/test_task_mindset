import requests
import cv2

img = cv2.imread('..\\DataForOCR\\' + '0.jpeg')

print( requests.get('https://latest.dbrain.io/recognize').status_code)
