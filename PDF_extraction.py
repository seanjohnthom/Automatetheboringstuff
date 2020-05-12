#import pypdf
import PyPDF2

#open the pdf file
pdf_file = open('meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
reader.numPages

#read the whole pdf
#page = reader.getPage(0)
#print(page.extractText())
#for pageNum in range(reader.numPages):
    #print(reader.getPage(pageNum).extractText())

#combine pdf files
pdf_1 = open('meetingminutes.pdf', 'rb')
pdf_2 = open('meetingminutes2.pdf', 'rb')
reader_1 = PyPDF2.PdfFileReader(pdf_1)
reader_2 = PyPDF2.PdfFileReader(pdf_2)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader_1.numPages):
    page = reader_1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader_2.numPages):
    page = reader_2.getPage(pageNum)
    writer.addPage(page)

combined_pdf = open('combined.pdf', 'wb')
writer.write(combined_pdf)
combined_pdf.close()
pdf_2.close()
pdf_1.close()
