## Importing the required dependencies
from socket import *
from pickle import loads

def server(ip : str, port : int):
    ## Starts socket instance and makes the socket reuseable,
    ## binds the socket to ip address $ip on port 5555 then listens
    ## and accepts connection from one client
    serve = socket(AF_INET, SOCK_STREAM)
    serve.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serve.bind((ip, 5555))
    print('binded to {} at port {}\n'.format(ip, port))

    serve.listen(1)
    conn, addr = serve.accept()
    print('accepted connection from client on address {}\n'.format(addr))

    if conn:
        ## If the connection is successfull start the main loop
        
        while True:
            ## The programs main loop, it sends commands to the server while making sure
            ## that the program does not get terminated after receiving output from the server
            command = input('')

            if command == 'quit':
                ## Terminates the program when the given command is 'quit'
                print('disconnecting...')
                serve.close()
                quit()
            
            else:
                ## Sends command to the server and displays output and execution status
                conn.sendall(command.encode('utf-8'))
                data = conn.recv(1024)
                try:
                    info = loads(data)
                    print('status  :', info[0])
                    print(info[1])
                
                except:
                    print('status  : failed')
                    continue

if __name__ == '__main__':
    ## Execution starts here
    print('starting the server')
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
    
    ## The server function is invoked, this function is responsible
    ## this function wait's for a connection from the client, accepts
    ## the said connection and then it can be used to run commands remotely
    server(ip, port)
