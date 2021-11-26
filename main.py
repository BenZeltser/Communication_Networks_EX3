import socket
from socket import *
import sys
'''Set host name.'''
host = socket.gethostname()
'''Set port number.'''
port = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
'''set host IP and Port number for the acceptance socket.'''
serverSocket.bind(socket.gethostname(),port)
''' get 1 TCP call each time as defined.'''
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    ''' Accept connection by the client'''
    connectionSocket, addr = serverSocket.accept()
    try:
        '''Get a information from the client through the socket and Decode it. set cap to 1KB per message.'''
        message =  connectionSocket.recv(1024).decode('utf-8')
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
