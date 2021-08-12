from PIL import Image

f = open('cat.jpg','rb')
bytess = f.readlines()
f.close()

new_bytes = b''
for _ in bytess:
    new_bytes += _



b = open('downloaded_file.txt','wb')
b.write(new_bytes)
b.close()

path_to_file = 'downloaded_file.txt'
save_path = path_to_file.replace('.txt', '.jpg')
with open(path_to_file, 'rb') as textfile:
    bytestring = textfile.read()

with open(save_path, 'wb') as imagefile:
    imagefile.write(bytestring)

image = Image.open(save_path)

