pip install PyPDF2
from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))

for i in range(n):
    name = input(f"Enter the name of pdf {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()

print("PDFs merged successfully!")
