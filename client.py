import socket

# get hostname of machine where script is running 
host = socket.gethostname() 
# The same port as used by the server
port = 12345                   
# create new socket using the given address family, arguments are default anyway
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port))
s.send(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
