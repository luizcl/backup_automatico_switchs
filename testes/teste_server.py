import socket

class Server:
        switch_name = ""
        software = ""
        version = ""
        model = ""
        warranty = False
        manufacturer = ""
        stacks = ""
        ip = ""

        def __init__(self, switch_name, software, version, model, warranty, manufacturer, stacks, ip):
            self.switch_name = switch_name
            self.software = software
            self.version = version
            self.model = model
            self.warranty = warranty
            self.manufacturer = manufacturer
            self.stacks = stacks
            self.ip = ip


# Captura o IP do servidor que está rodando o código
hostname = socket.gethostname()
#Seta um atributo estático na classe Server
setattr(Server, 'tftp_server', socket.gethostbyname(hostname))

servers = []
#Arquivo de lista de switches
file_name = '../lista-de-switches.csv'
#Leitura de arquivo CSV com o delimitador ';'
f = open('lista-de-switchs.txt', 'r')
#Lê todas as linhas pulando a primeira
lines = f.readlines()[1:]
for line in lines:
    # Retira a quebra de linha
    aux = line.replace('\n', "")
    # Divide em várias strings separando por ';'
    rows = aux.split(';')
    srv = Server(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
    servers.append(srv)
f.close()
for srv in servers:
    print("================================")
    print("Switch Name: " + srv.switch_name)
    print("Software: " + srv.software)
    print("Version: " + srv.version)
    print("Model: " + srv.model)
    print("Warranty: " + str(srv.warranty))
    print("Manufacturer: " + srv.manufacturer)
    print("Stacks: " + srv.stacks)
    print("IP: " + srv.ip)
    print("TFTP Server: " + Server.tftp_server)
    print("===================================")
    print()
