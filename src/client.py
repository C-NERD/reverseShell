## Importing our dependencies from the python standard library
from socket import *
from pickle import loads, UnpicklingError

def client(ip, port):

    try:
        ## Starts the socket instance and connects to the server using ip address $ip on
        ## port $port. It ensures the connection is successfull else the program
        ## is terminated.
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
        print('connected to {} at port {}\n'.format(ip, port))

    except:
        print('Error: unable to connect to {} at port {}'.format(ip, port))
        quit(-1)

    while True:
        ## The programs main loop, it sends commands to the server while making sure
        ## that the program does not get terminated after receiving output from the server
        command = input('')
        if command == 'quit':
            ## Terminates the program when the given command is 'quit'
            print('disconnecting...')
            quit()
        
        else:
            ## Sends command to the server and displays output and execution status
            client.sendall(command.encode('utf-8'))
            data = client.recv(1024)
            try:
                info = loads(data)
                print('status  :', info[0])
                print(info[1])
            
            except:
                print('status  : failed')
                continue

if __name__ == '__main__':
    ## Execution starts here
    ip = input('ipaddress -> ')

    try:
        ## Makes sure the given port is an integer between 1000 and 50000
        port = int(input('port -> '))

        if port < 1000 or port > 50000:
            print('Error: the port is meant to be a number from 1000 to 50000')
            quit(-1)
    except:
        print('port {} is not an integer'.format(port))
        quit(-1)

    ## Invokes the client function with the parameters ip and port.
    ## This function is responsible for connecting to the server, sending and
    ## receiving commands to and from the server.
    client(ip, port)
