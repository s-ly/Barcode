# BarCode ver 1.0
# Программа для распознавания штрихкода из Google диска.

# для Google
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# для распознавания 
from pyzbar.pyzbar import decode
from PIL import Image  # pip install Pillow

print('BarCode ver 1.0')
print('Авторизация Google API ...')

# авторизация Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

print('Авторизация Google API получена.')

# папка Вагиза
file_list = drive.ListFile({'q': "'1ECokctvywhiGuJKR0aZJtl_WxL67hkG5' in parents"}).GetList() 


img_sum = 0
for file1 in file_list:
    img_sum = img_sum + 1
print('Всего файлов ' + str(img_sum))
print()


i = 0
barcode_sum = 0
for file1 in file_list:
    i = i + 1
    print('файл ' + str(i) + 'из ' + str(img_sum))
    # Печать имени и id каждого файла в папке
    print('title: %s, id: %s' % (file1['title'], file1['id']))

    file_obj = drive.CreateFile({'id': file1['id']})
    # file_obj.GetContentFile(file1['title']) # записать с реальным именем
    file_obj.GetContentFile('img_temp.jpg') # записать с общим для всех именем

    image_barcode = Image.open('img_temp.jpg')
    # image_barcode = Image.open(file_name)
    img_decode = decode(image_barcode)

    # x = img_decode[0].data.decode('utf-8')
    if img_decode:
        print('штрихкод '+ img_decode[0].data.decode('utf-8'))
        barcode_sum = barcode_sum + 1
        print('обнаруженно штрихкодов: ' + str(barcode_sum))
    else:
        print('нет штрихкода')
    # print(x)
    # if (img_decode[0] != None):
    #     print(img_decode[0].data.decode('utf-8'))

print('ИТОГО штрихкодов: ' + str(barcode_sum))