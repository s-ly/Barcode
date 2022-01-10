# BarCode ver 1.0
# Программа для распознавания штрихкода из Google диска.

# для Google
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# для распознавания 
from pyzbar.pyzbar import decode
from PIL import Image  # pip install Pillow

# ctypes.windll.kernel32.SetDllDirectoryW(None)

def get_url () -> str:
    """Получение URL"""
    my_url = input('Вставте ссылку и нажмите Ввод: ')
    start_index = 39
    my_url = my_url[start_index:] # срез первой части

    # поиск индекса концовки, если не найдёт, то -1
    end_index = my_url.find('?usp=sharing') # поиск индекса концовки
    if end_index != -1:
        my_url = my_url[:end_index] # срез концовки если есть
        
    return my_url


print('\nBarCode ver 1.0')
print('Авторизация Google API ...')

# авторизация Google
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

print('Авторизация Google API получена.')
url_part = get_url()
file_list = drive.ListFile({'q': f"'{url_part}' in parents"}).GetList()

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

print('\nИТОГО штрихкодов: ' + str(barcode_sum))
input('Нажмите Ввод для завершения')