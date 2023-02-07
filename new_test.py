import PyPDF2
from pdf2image import convert_from_path
myfile=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/crash_course.txt","r",encoding="utf-8")
for index, line in enumerate(myfile):
	print("Line{}: {}".format(index,line.strip()))


