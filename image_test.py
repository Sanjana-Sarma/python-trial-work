from pdf2image import convert_from_path
import PyPDF2
images=convert_from_path("C:/Users/angel/OneDrive/Desktop/python trial/1.pdf")
for i, image in enumerate(images):
	imgfile="image"+str(i)+".png"
	image.save(imgfile,"PNG")
