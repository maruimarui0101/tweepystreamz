import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print (host , port)
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:

    try:
        data = conn.recv(4096)

        if not data: continue

        print ("Client Says: " +str(data))
        # Send acknowledgement
        conn.sendall(b"Server Says:hi")

    except socket.error:
        print ("Error Occured.")
        break

conn.close()