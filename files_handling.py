from os import listdir, rename, mkdir

print(listdir('.'))

mkdir('./Sheets')

for sheet in listdir('.'):
    if('.Xlsx' in sheet.title()):
        #   put file title in a cell
        #   change a cell
        #   rename the file
        print(sheet.title())