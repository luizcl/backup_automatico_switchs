f = open('lista-de-switchs.txt', 'r')
lines = f.readlines()[1:]
for line in lines:
    aux = line.replace('\n', "")
    aux_split = aux.split(';')
    print(line[0])
f.close()