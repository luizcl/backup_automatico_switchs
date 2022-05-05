from cryptography.fernet import Fernet

key = '7JHc_3DxzXqQtCJvwgY4mGms38ay7zPsxZUPIFqaYS0='

fernet = Fernet(key)
with open('../User.enc', 'rb') as enc_file:
    encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('teste.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    dec_file.close()
enc_file.close()