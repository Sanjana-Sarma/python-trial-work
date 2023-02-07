import PyPDF2
from pdf2image import convert_from_path
file1=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/1.pdf","r",encoding="utf-8",errors="ignore")
lines=file1.readlines()
j=0
i=0
while lines:
	for index,line in enumerate(lines): 
		line=lines[i].strip()
		image=convert_from_path("1.pdf")
		img="image"+str(i)+".png"
		image.save(img,"PNG")
	j+=1
	i+=1
file1.close()
