# Echo client program 
import socket

HOST = '10.0.0.1'    # The remote host
PORT = 9000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
buffer = 'A'*100
s.send(buffer) 
data = s.recv(1024)
s.close()
print 'Received', repr(data)
