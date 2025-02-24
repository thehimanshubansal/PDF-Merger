import os
from PyPDF2 import PdfWriter

merge = PdfWriter()

fileslist = [i for i in os.listdir() if i.endswith(".pdf")]

for file in fileslist:
    merge.append(file)

b = input("Enter the name of the merged file: ")
merge.write(f"{b}.pdf")
merge.close()

c = input("Do you want to view {b} (y/n): ")
if c == 'y':
    os.startfile(f"{b}.pdf")
else:
    print("Have a nice day!")