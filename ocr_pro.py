from PIL import Image, ImageEnhance
import pytesseract

def initTable(threshold=140):
	table = []
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)
	return table

def ocrCaptcha():
	retrytime = 0
	image = Image.open('captcha.gif')
	enhancer = ImageEnhance.Contrast(image)
	image = enhancer.enhance(4)
	image = image.convert('L')
	binaryImage = image.point(initTable(), '1')
	while retrytime<5:
		ltext = pytesseract.image_to_string(binaryImage, lang='eng', config='-psm 7 number')
		if len(ltext) == 5:
			break
		retrytime = retrytime+1
		print('try '+retrytime+' '+ltext)
	return ltext
