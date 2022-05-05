import socket

class Switch:
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
setattr(Switch, 'tftp_server', socket.gethostbyname(hostname))