import PyPDF2
myFile=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/Python Crash Course, 2nd Edition (Eric Matthes) (z-lib.org).pdf","rb")
output_file=open("C:/Users/angel/OneDrive/Desktop/TEXTBOOKS/COMPUTER PROGRAMMING/PYTHON/python_work/crash_course.txt","w",encoding="utf-8")
pdfreader=PyPDF2.PdfFileReader(myFile)
numofpages=pdfreader.numPages
print("No. of Pages:",numofpages)
for i in range(numofpages):
    pageext=pdfreader.getPage(i)
    textext=pageext.extractText(i)
    output_file.write(textext)
output_file.close()
myFile.close()
    