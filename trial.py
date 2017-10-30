import socket
obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "192.168.1.26"
PORT = 23
obj.connect((HOST,PORT))
def sendCmd(obj,cmd):
    
    obj.write(cmd)
    print obj.read(20)
