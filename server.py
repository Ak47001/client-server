import socket
import os
import time
s= socket.socket()
s.bind(('',8779))
s.listen(1)
c,addr = s.accept()
print("Connected sucesfully ",c,addr)
file1= c.recv(1024).decode('utf-8')
print(file1)
with open(file1,'w+') as f:
	c.sendall(bytes(time.ctime(os.path.getmtime(file1)),'utf-8'))
	while True:
		bi = c.recv(1024)
		if not bi:
			break
		print(bi)
		f.write(bi.decode('utf-8'))
	f.close()
c.close()
