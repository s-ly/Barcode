from pyzbar.pyzbar import decode
from PIL import Image
# image_barcode = Image.open('barcode_07m.jpg')
image_barcode = Image.open('images/barcode_11m.jpg')
decode = decode(image_barcode)
print(decode[0].data.decode('utf-8'))