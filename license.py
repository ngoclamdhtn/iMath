import hashlib
import winreg
import psutil
import subprocess
import base64
from cryptography.fernet import Fernet
from datetime import datetime

def get_drive_serial_number():
    st=subprocess.check_output('wmic bios get serialnumber').decode("utf-8")
    st=st.replace("SerialNumber","")
    st = ''.join(st.splitlines())
    st=st.replace(" ","")
    return st

def encrypt_string(s):
    key=b'ApDVZwk8Rp-ExD0Mupg5BC--uYlR7FC5rKn6qLEADpA='
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(s.encode('utf-8'))

    str_text=str(encrypted_text)
    len_str_text=len(str_text)
    encrypted_text=str_text[2:len_str_text-1]

    return encrypted_text

def decrypt_string(encrypted_text):
    key=b'ApDVZwk8Rp-ExD0Mupg5BC--uYlR7FC5rKn6qLEADpA='
    cipher_suite = Fernet(key)
    bytes_string = encrypted_text.encode('utf-8') 
    decrypted_text = cipher_suite.decrypt(bytes_string).decode('utf-8')
    return decrypted_text

def encrypt_serial_number():
    text=encrypt_string(get_drive_serial_number())
    return text

def md5_encode(input_string):
    # Tạo một đối tượng hash MD5
    md5_hash = hashlib.md5()

    # Cập nhật đối tượng hash với dữ liệu đầu vào (phải là dạng bytes)
    md5_hash.update(input_string.encode('utf-8'))

    # Trả về giá trị mã hóa MD5 dưới dạng hex
    return md5_hash.hexdigest()

#Tạo khóa registry
def create_registry_key(value_data):
    key_path = r"SOFTWARE\iMath"
    value_name = "iMathApp"

    # Mở hoặc tạo khóa registry
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

    # Đặt giá trị cho khóa
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
    return

#Tạo khóa registry
def create_reg_thongtin(value_name, value_data):
    key_path = r"SOFTWARE\iMath"
     # Mở hoặc tạo khóa registry
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

    # Đặt giá trị cho khóa
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value_data)
    return

#Đọc khóa registry
def read_reg_thongtin(value_name):
    try:

        key_path = r"SOFTWARE\iMath"        

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)

        # Đọc giá trị
        value, _ = winreg.QueryValueEx(key, value_name)
        # Đóng key
        winreg.CloseKey(key)       

    except Exception as e:
        value=""
    return value  

   
#Đọc registry
def read_registry_value():
    try:

        key_path = r"SOFTWARE\iMath"
        value_name = "iMathApp"

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)

        # Đọc giá trị
        value, _ = winreg.QueryValueEx(key, value_name)
        # Đóng key
        winreg.CloseKey(key)       

    except Exception as e:
        value=""
    return value

def kiemtra_banquyen():
    ketqua = False
    try:
        key_registry=read_registry_value()
        key = decrypt_string(key_registry)
        t=len(key)

        #Lấy ngày tháng
        str_day=key[t-10:t]
        Date_start  = datetime.strptime(str_day, "%d/%m/%Y")
        dayLicense = datetime.now()- Date_start
        dayLicense =dayLicense.days

        #Trả về kết quả kiểm tra        
        if dayLicense<=365:
            ketqua = True        
    except Exception as e:
        ketqua = False        
    return ketqua

def check_banquyen(key):
    ketqua = False
    try:        
        key = decrypt_string(key)
        t=len(key)

        #Lấy ngày tháng
        str_day=key[t-10:t]
        Date_start  = datetime.strptime(str_day, "%d/%m/%Y")
        dayLicense = datetime.now()- Date_start
        dayLicense =dayLicense.days

        #Trả về kết quả kiểm tra        
        if dayLicense<=365:
            ketqua = True         
    except Exception as e:
        ketqua = False        
    return ketqua

def so_ngay_banquyen():
    so_ngay = 0
    try:
        key_registry=read_registry_value()
        key = decrypt_string(key_registry)
        t=len(key)

        #Lấy ngày tháng
        str_day=key[t-10:t]
        Date_start  = datetime.strptime(str_day, "%d/%m/%Y")
        dayLicense = datetime.now()- Date_start
        dayLicense =dayLicense.days

        #Trả về kết quả kiểm tra        
        if dayLicense<=365:
            so_ngay = 365-dayLicense
    except Exception as e:
        so_ngay = 0       
    return so_ngay







