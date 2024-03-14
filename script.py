import zipfile
from itertools import product
import os

def extract_zip(zipfilename, password):
    try:
        with zipfile.ZipFile(zipfilename, 'r') as zip_file:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            print("Contents of the zip file:")
            for fileinfo in zip_file.infolist():
                print(f"Reading file: {fileinfo.filename}")
                with zip_file.open(fileinfo.filename, pwd=bytes(password, 'utf-8')) as file:
                    if fileinfo.filename.endswith('.txt'):
                        print(file.read().decode('utf-8'))

            return True
    except zipfile.BadZipFile:
        print("Error: Bad Zip File.")
        return False
    except RuntimeError as e:
        if 'incorrect password' in str(e):
            return False
        print(f"Runtime error: {e}")
        return False

def brute_force(zipfilename):
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+"
    max_length = 8 

    try:
        with zipfile.ZipFile(zipfilename, 'r') as zip_file:
            for length in range(1, max_length + 1):
                for attempt in product(charset, repeat=length):
                    password = ''.join(attempt)
                    if extract_zip(zipfilename, password):
                        print(f"Password found: {password}")
                        return password
            print("Password not found.")
            return None
    except FileNotFoundError:
        print(f"File not found: {zipfilename}")
        return None
    except zipfile.BadZipFile:
        print("Error: Bad Zip File.")
        return None

zipfilename = 'TryMe.Zip'  

password = brute_force(zipfilename)
