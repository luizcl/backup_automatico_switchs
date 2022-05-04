import socket
import csv

class Server:
        pass

switch_name = ""
software = ""
version = ""
model = ""
warranty = False
manufacturer = ""
stacks = ""
ip = ""


hostname = socket.gethostname()
setattr(Server, 'tftp_server', socket.gethostbyname(hostname))

file_name = "lista-de-switchs.csv"
file = open(file_name, "r")
csv_file =
for line in f:
        i = 1
        a = 2
f.close()


print("Switch Name: " + switch_name)
print("Software: " + software)
print("Version: " + version)
print("Model: " + model)
print("Warranty: " + str(warranty))
print("Manufacturer: " + manufacturer)
print("Stacks: " + stacks)
print("IP: " + ip)
print("TFTP Server: " + Server.tftp_server)
