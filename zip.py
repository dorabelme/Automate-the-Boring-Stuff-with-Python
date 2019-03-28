import zipfile, os

os.chdir('/Users/dorabelme/Downloads')
exampleZip = zipfile.ZipFile('5333b.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('5333b/pic1.jpg')
spamInfo.file_size
spamInfo.compress_size

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()


os.chdir('/Users/dorabelme/Downloads')
exampleZip = zipfile.ZipFile('5333b.zip')
exampleZip.extractall()
exampleZip.close()