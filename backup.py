import socket

class User:
    _user_name = ""
    _user_password = ""
    def __init__(self, name, password):
        self._user_name = name
        self._user_password = self.decrypt(password)

    def get_name(self):
        return self._user_name

    def decrypt(self, password):
        passwd = ""
        lenght = range(int(len(password) / 2))
        for i in lenght:
            passwd = passwd + chr(ord(password[2 * i + 1]) - 7)
        return passwd

class Server:
    _swithc_name = ""
    _software = ""
    _version = ""
    _model = ""
    warranty = False
    _manufacturer = ""
    _stacks = ""
    _ip = ""

    def set_tftp_ip(self):
        hostname = socket.gethostname()
        self._ip = socket.gethostbyname(hostname)

def main():
    usr = User("Luiz", "123435434567567")
    print(usr.get_name())

if __name__ == "__main__":
    main()