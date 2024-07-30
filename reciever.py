import socket
import datetime
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_addr="127.0.0.1"       #localhost ip     #reciever ip
port_no=7072     #our own made port no        # 0-65353 are total no of ports available and 0-1023 are TCP ports and are reserved
complete_addr=(ip_addr,port_no)
s.bind(complete_addr)       # it means that register with the given address   
print("I am listening....\n")

condit=True
while condit:
    Data=s.recvfrom(100)        #at a time can recieve 100 characters
    Message=Data[0]
    Message=Message.decode('ascii')
    sender_addr=Data[1]
    sender_ip_addr=Data[1][0]
    now = datetime.datetime.now()
    time=now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Message}\t[{time}]")
    file=open(sender_ip_addr+'.txt','a')
    file.write(f"{Message}\t[{time}]\n")
    file.close()
    mess=input("Enter your reply messsage: ")
    message_encrypt=mess.encode('ascii')
    s.sendto(message_encrypt,sender_addr)
    def perm():
        permission=input("Do you want to quit? Y/N : ")
        if permission=="Y" or permission=="y":
            condit=False
        elif permission=="N" or permission=="n":
            mess=input("Enter your reply messsage: ")
            message_encrypt=mess.encode('ascii')
            s.sendto(message_encrypt,sender_addr)
            perm()
    perm()
    