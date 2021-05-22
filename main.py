import random
from time import sleep


print("")
print("")
print("")
print("\033[1;36;40m \n ")
print("▒█▀▀▀ ░█▀▀█ ▒█▀▄▀█ ░█▀▀█")
print("▒█▀▀▀ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█")
print("▒█░░░ ▒█░▒█ ▒█░░▒█ ▒█░▒█")
print("\033[1;35;40m 𝒞𝑅𝐸𝒜𝒯𝐸𝒟 𝐵𝒴 𝐻𝒰𝒩𝒯𝐸𝑅 \n")
print("")
print("")
print("\033[1;32;40m ꜰᴀᴋᴇ ᴍᴀɪʟ ɢᴇɴᴇʀᴀᴛᴏʀ \n")
print("                   Type -FM to get one")
print("                   Type exit to close it")
print("\033[1;36;40m  \n")

def mainfunc():
    user = input("User > ")
    if user == "-FM":
        name = input("Type a random word > ")
        rn = random.randint(1,10000)
        rl = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rl_2 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        rl_3 = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        sleep(1)
        print("")
        print("E-Mail > " "\033[1;32;40m "+ name + str(rn) + rl_2 + rl_3 + "@" + rl + ".mail.com \n")
        print("\033[1;36;40m  \n")
        return mainfunc()
        
    if user == "exit":
        exit()     
        
    else:
        print("\033[1;31;40m \n")
        print(user + " was not found.")
        print("\033[1;36;40m  \n")
        return mainfunc()
        
mainfunc()