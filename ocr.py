from PIL import Image
import pytesseract

def ocrCaptcha():
	image = Image.open('captcha.gif')
	ltext = pytesseract.image_to_string(image, lang='eng', config='-psm 7')
	return ltext
