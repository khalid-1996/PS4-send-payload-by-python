import socket
import sys
import time


print()
HOST = input("PS4 IP : ") # The server's hostname or IP address
PORT = int (input("PORT NUMBER : "))     # The port used by the server
SEPARATOR = "<SEPARATOR>"

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    s.connect((HOST, PORT))
    print(f"[+] Connecting to {HOST}:{PORT}")
    s.sendall(b"hello")
    time.sleep(1)
    print()
    print("[+] Connected Successfully") 
    print()
except:
    print(f"[+] Connecting to {HOST}:{PORT}")
    print()
    time.sleep(1)
    print()
    print("PS4 : Unable to connect")
    print()
    exit(0)
    
def main():
       menu()


#################################


def menu():
    print()

    print("devlop by : @kk.6c")
    print()
    print("************ Welcome **************")
    print()

    choice = input("""
      1: upload payloads
      2: tools for ps4
      3: linux  
      4: games hack menu 
      Q: Logout
   Please enter your choice: """)

    if choice == "1" or choice =="١":
        upload()
    elif choice == "2" or choice =="٢":
        tools()
    elif choice == "3" or choice =="٣":
        print(" opps ")
    elif choice == "4" or choice =="٤":
        games()
    elif choice=="q" or choice=="Q":
        print("شكرا لاستاخدام الاسكربت  ")
        sys.exit

    else:
        print("Error : only use Numbers")
        print("try Agen")
        menu()


#######################################




def upload(): 
    print()
    print("################### upload payload ###############")
    print()


    uploads = input(" drage payload here : ")

    f = open(uploads,'rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  
    




#######################################

def ftp(): 
    print()
    print("################### FTP ###############")
    print()
    f = open('bin/ftp.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close     
    
    
#######################################

def orbis(): 
    print()
    print("################### Orbis Toolbox ###############")
    print()
    
    f = open('bin/Orbis-Toolbox-900.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close                     

#############################################################################

def games(): 
    print()
    print("************ games hack menu  **************")
    print()

    choice = input("""
      1: GTA V 1.33 mode menu
      2: RED Dead (Not Working)
      Q: Logout
   Please enter your choice: """)

    if choice == "1" or choice =="١":
        gta()
    elif choice == "2" or choice =="٢":
        ftp()
    
    elif choice=="q" or choice=="Q":
        print("thx for using my  ")
        sys.exit

    else:
        print("Error : only use Numbers")
        print("try Agen")
        menu()

                   
def gta(): 
    f = open('bin/gg.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close    
    
#############################################################################

    
def tools(): 
    print()
    print("************ TOOLS FOR PS4  **************")
    print()

    choice = input("""
      1: FTP SERVER 
      2: PS4 debug  
      3: webRTE 
      4: Orbis Toolbox
      5: MiraLoader
      6: disable updates for ps4
      7: app2usb
      8: show password for your PS4 user
      Q: Logout
   Please enter your choice: """)

    if choice == "1" or choice =="١":
        ftp()
    elif choice == "2" or choice =="٢":
        debug()
    elif choice == "3" or choice =="٣":
        webRTE()
    elif choice == "4" or choice =="٤":
        orbis()
    elif choice == "5" or choice =="٣":
        MiraLoader()
    elif choice == "6" or choice =="٣":
        disableupdates()
    elif choice == "7" or choice =="٣":
        app2usb()   
    elif choice == "8" or choice =="٣":
        parental()   
    elif choice=="q" or choice=="Q":
        print("thx for using my  ")
        sys.exit

    else:
        print("Error : only use Numbers")
        print("try Agen")
        menu()


   
def debug(): 
    f = open('bin/ps4debug.bin'  ,'rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close   
    
    webRTE
    
def webRTE(): 
    f = open('bin/webRTE.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  
    
   
def MiraLoader(): 
    f = open('bin/MiraLoader.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  
      
  
def disableupdates(): 
    f = open('bin/disableupdates.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  
    

    
def app2usb(): 
    f = open('bin/app2usb.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  

def parental(): 
    f = open('bin/ps4-parental-controls.bin','rb')
    l = f.read()
    while l:
        s.send(l)
        l = f.read()
    f.close()
    s.close  
    
    
   






main()

