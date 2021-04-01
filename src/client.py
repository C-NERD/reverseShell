from socket import *
from pickle import loads, UnpicklingError

def client(ip, port):

    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
        print('connected to {} at port {}\n'.format(ip, port))

    except:
        print('Error: unable to connect to {} at port {}'.format(ip, port))
        quit(-1)

    while True:

        command = input('')
        client.sendall(command.encode('utf-8'))

        if command == 'quit':
            print('disconnecting...')
            quit()

        data = client.recv(1024)
        try:
            info = loads(data)
            print('status  :', info[0])
            print(info[1])
        
        except:
            print('status  : failed')

if __name__ == '__main__':
    ip = input('ipaddress -> ')

    try:
        port = int(input('port -> '))
    except:
        print('Error: the port is meant to be a number from 1000 to 60000')
        quit(-1)

    client(ip, port)
