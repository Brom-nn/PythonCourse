import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8787
s.bind((host, port))
s.listen(5)
while True:
    conn, addr = s.accept()
    f = conn.recv(1024)
    print(f.decode())
    conn.close()