import socket

def server(m):
    s = socket.socket()
    host = socket.gethostname()
    port = 55155
    s.bind((host,port))
    s.listen(1)
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    c.send(bytes(m))
    c.close()
    s.close()


def client():
    s = socket.socket()
    host = socket.gethostname()
    port = 55155
    print host
    s.connect((host,port))
    m = s.recv(102400).decode('utf-8')
    s.close()
    return m