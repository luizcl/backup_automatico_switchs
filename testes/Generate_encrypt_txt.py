from cryptography.fernet import Fernet

key = '7JHc_3DxzXqQtCJvwgY4mGms38ay7zPsxZUPIFqaYS0='

fernet = Fernet(key)
with open('User.txt', 'rb') as file:
    original = file.read()
    encrypted = fernet.encrypt(original)
    with open('../User.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
encrypted_file.close()
file.close()
