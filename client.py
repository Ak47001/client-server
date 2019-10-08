
import socket
import sys

#read file
filename = 'filename.txt'
# client program using python
s = socket.socket()
ip = ''
port = 8777
s.connect((ip,port))
print("Successfully connected to ",ip)
with open(filename,'r') as fd:
	str = fd.read(1024)
	s.sendall(bytes(filename,'utf-8'))
	print("Last Modified time",s.recv(1024))
	while(str):
		s.send(bytes(str,'utf-8'))
		str=fd.read(1024)	
	
fd.close()	
s.close()


