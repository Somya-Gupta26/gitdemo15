import socket       #library or module that is an endpoint through which message will be sent and will be recieved
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)     # s object=socket module has a socket class

#socket.AF_INET ----> Send my message through the internet
#socket.SOCK_DGRAM ----> Represents protocol (either could be TCP or UDP)

target_ip="127.0.0.1"       #localhost ip and is used by a computer to refer to itself      #reciever ip
target_port=7072        #you can enter any port no. according to you
target_addr=(target_ip,target_port)
condition=True
while condition:
    message=input("Please enter your message: ")
    message_encrypted=message.encode('ascii')
    s.sendto(message_encrypted,target_addr)
    print("Your message is sent ...")
    data=s.recvfrom(100)
    Mess=data[0]
    Mess=Mess.decode('ascii')
    print("Your recieved mesage is: ",Mess)
    permit=input("Do you want to exit the program? Y/N  : ")
    if permit=="Y" or permit=="y":
        condition=False
    elif permit=="N" or permit=="n":
        data=s.recvfrom(100)
        Mess=data[0]
        Mess=Mess.decode('ascii')
        print("Your recieved mesage is: ",Mess)
    
