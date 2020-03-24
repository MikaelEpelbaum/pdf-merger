from pikepdf import Pdf
from os import path, listdir

print("enter files directory path")
directory = str(input())
print("enter your output file name, without '.pdf'")
name = str(input())
files = []

for file in listdir(directory):
    if file.endswith('pdf') and 'chapter' not in file:
        files.append(path.join(directory, file))

files.sort(key=path.getctime)

if not files[-1].startswith('Scan'):
    files = files[-1:] + files[:-1]

pdf = Pdf.new()

for file in files:
    src = Pdf.open(file)
    pdf.pages.extend(src.pages)

pdf.save(path.join(directory, name) + '.pdf')
