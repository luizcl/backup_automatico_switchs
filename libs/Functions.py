from cryptography.fernet import Fernet
from paramiko import SSHClient

from backup_automatico_switchs.Switch import Switch
from backup_automatico_switchs.User import User
from backup_automatico_switchs.libs.Key_generate import key


def get_all_users():
    usr = []

    fernet = Fernet(key)
    with open('User.enc', 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        str_aux = str(decrypted)
        aux = str_aux.split("\\r\\n")
        aux = aux[1:]
        for str_line in aux:
            str_arr = str_line.split(';')
            usr.append(User(str_arr[0], str_arr[1]))
    enc_file.close()
    return usr


def get_all_switches():
    sws = []
    # Arquivo de lista de switches
    file_name = 'lista-de-switches.csv'

    f = open(file_name, 'r')

    # Lê todas as linhas pulando a primeira
    lines = f.readlines()[1:]
    for line in lines:
        # Retira a quebra de linha
        aux = line.replace('\n', "")

        # Divide em várias strings separando por ';'
        rows = aux.split(';')

        srv = Switch(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
        sws.append(srv)
    f.close()
    return sws


def ssh_connect(users, switches):
    client = SSHClient()
#    ssh.connect(server, username=username, password=password)
#    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)

