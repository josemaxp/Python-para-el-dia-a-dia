from pdf2docx import Converter

pdf_file = input("Introduce la ubicación del pdf: ") #Ej: C:\Users\x\Desktop\x.pdf
docx_file = input("Introduce la ubicasción de salida del word: ") #Ej: C:\Users\x\Desktop\x.docx
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()