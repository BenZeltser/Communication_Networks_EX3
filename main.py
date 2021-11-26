import socket
from socket import *
import sys

host = socket.gethostname() '''Set host name.'''
port = 6789 '''Set port number.'''
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(socket.gethostname(),port) '''set host IP and Port number for the acceptance socket.'''
serverSocket.listen(1) ''' get 1 TCP call each time as defined.'''
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  ''' Accept connection by the client'''
    try:
        message =  connectionSocket.recv(1024).decode('utf-8') '''Get a information from the client through the socket and Decode it. 
                                                                set cap to 8KB per message.'''
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  "OK "
        connectionSocket.send(bytes(outputdata, 'utf-8'))
        # Send one HTTP header line into socket
        # Fill in start
        ''' $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
# Send response message for file not found
# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding
# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
# Fill in end
while True:d     # Send one HTTP header line into socket
        # Fill in start
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
# Send response message for file not found
# Fill in start
# Fill in end
# Close client socket
# Fill in start
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding
