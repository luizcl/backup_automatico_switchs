from cryptography.fernet import Fernet
from libs.Key_generate import key


class User:
    _user_name = ""
    _user_password = ""

    def __init__(self, name, password):
        self._user_name = name
        self._user_password = password

    def get_name(self):
        return self._user_name


class UserFile(User):
    def __int__(self, name, password):
        fernet = Fernet(key)
        with open('User.enc', 'rb') as enc_file:
            encrypted = enc_file.read()
            decrypted = fernet.decrypt(encrypted)
            str_aux = str(decrypted)
            aux = str_aux.split("\\r\\n")
            str_line = aux[1]
            str_arr = str_line.split(';')
            self._user_name = str_arr[0]
            self._user_password = str_arr[1]

        enc_file.close()
