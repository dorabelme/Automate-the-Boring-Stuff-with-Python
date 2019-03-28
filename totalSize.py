import os


totalSize = 0
for filename in os.listdir('/Users/dorabelme'):
    totalSize = totalSize + os.path.getsize(os.path.join('/Users/dorabelme', filename))

print(totalSize)

