# import requests
# from googleDriveFileDownloader import googleDriveFileDownloader
# gdownloader = googleDriveFileDownloader()
# # gdownloader.downloadFile("https://drive.google.com/uc?id=1O4x8rwGJAh8gRo8sjm0kuKFf6vCEm93G&export=download")
# # gdownloader.downloadFile("https://drive.google.com/drive/folders/1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5?usp=sharing")
# gdownloader.downloadFile("https://drive.google.com/drive/folders/uc?id=1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5&export=download")

from google_drive_downloader import GoogleDriveDownloader as gdd

gdd.download_file_from_google_drive(file_id='1d1MdjIOIhQ4cCdDyjL7JicuegD5aXUN5',
                                    # dest_path='./data/mnist.zip',
                                    dest_path='./data/test',
                                    unzip=True)