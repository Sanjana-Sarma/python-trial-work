import PyPDF2
myFile=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/1.pdf","rb")
output_file=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/1.txt","w")
pdfReader=PyPDF2.PdfFileReader(myFile)
numofPages=pdfReader.numPages
print("No. of Pages:",numofPages)
for i in range(numofPages):
	page=pdfReader.getPage(i)
	text=page.extractText()
	output_file.write(text)
output_file.close()
myFile.close()