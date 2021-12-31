from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5' in parents"}).GetList()
# file_list = drive.ListFile({'q': "'1ECokctvywhiGuJKR0aZJtl_WxL67hkG5' in parents"}).GetList()
# print(file_list)
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
file_obj = drive.CreateFile({'id': '17ZamP8AUvDhWDchD7Gsurko1U4ZGVWpi'})
file_obj.GetContentFile('test1.txt')


# Initialize GoogleDriveFile instance with file id.
# file_obj = drive.CreateFile({'id': '<your file ID here>'})
# file_obj.GetContentFile('cats.png') # Download file as 'cats.png'.


# file6 = drive.CreateFile({'id': file5['id']})
# file6.GetContentFile('catlove.png') # Download file as 'catlove.png'.


# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from oauth2client.client import GoogleCredentials

# gauth = GoogleAuth()
# # gauth.LocalWebserverAuth()
# gauth.credentials = GoogleCredentials.get_application_default()
# drive = GoogleDrive(gauth)
# file_list = drive.ListFile(
#     {'q': "'1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5?' in parents"}).GetList()

# def create_and_upload_file(file_name='test.txt', file_content='Hey Dude!'):
#     try:
#         drive = GoogleDrive(gauth)

#         my_file = drive.CreateFile({'title': f'{file_name}'})
#         my_file.SetContentString(file_content)
#         my_file.Upload()

#         return f'File {file_name} was uploaded!Have a good day!'
#     except Exception as _ex:
#         return 'Got some trouble, check your code please!'

# def main():
#     print(create_and_upload_file(file_name='hello.txt', file_content='Hello Friend'))

# def main():
#     print('123')
#     file_list = drive.ListFile(
#     {'q': "'1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5?' in parents"}).GetList()

# if __name__ =='__main__':
#     main()