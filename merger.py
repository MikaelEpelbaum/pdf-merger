from pikepdf import Pdf
from os import path, listdir

print("enter files directory path")
directory = str(input())
print("enter your output file name, without '.pdf'")
name = str(input())
files = []

for file in listdir(directory):
    if file.endswith('pdf'):
        files.append(path.join(directory, file))

files.sort(key=path.getctime)

pdf = Pdf.new()

for file in files:
    src = Pdf.open(file)
    pdf.pages.extend(src.pages)

pdf.save(path.join(directory, name) + '.pdf')
