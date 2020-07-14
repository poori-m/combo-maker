passlist = input("please enter name of passlist: ")
user = input("please enter username: ")

combo = open("combo.txt","w+")
pasfile = open(passlist,"r")

for i in pasfile:
    temp = user + ":" + i
    combo.write(temp)

combo.close()
pasfile.close()
print("secessfuli!")
