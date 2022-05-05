from cryptography.fernet import Fernet

key = []
# string the key in a file
with open('.key', 'wb') as filekey:
    key.append(Fernet.generate_key())
    key.append(Fernet.generate_key())
    key.append(Fernet.generate_key())
    key.append(Fernet.generate_key())
    filekey.write(key)
filekey.close()