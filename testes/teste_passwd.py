password = "A#adc*!123"

passwd = ""
#for i, letter in enumerate(password):
    ### ord() function gives the ASCII code of a character
    #passwd = passwd + chr(ord(password[2*i+1]) - 7)

lenght = len(password)/2
i = 0
# while(i < lenght):
#     passwd = passwd + chr(ord(password[2 * i + 1]) - 7)
#     i+=1
lenght = range ( int( len(password)/2 ) )
for i in lenght:
    passwd = passwd + chr(ord(password[2 * i + 1]) - 7)
print(passwd)