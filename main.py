import socket
import requests_html
from requests_html import HTML
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
'''Set host name.'''
host = gethostname()
'''Set port number.'''
port = 6789
'''set host IP and Port number for the acceptance socket.'''
serverSocket.bind((host, port))
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
        message = connectionSocket.recv(1024).decode('utf-8')
        f = open(filename[1:])
        outputdata = connectionSocket.send(bytes(message, 'utf-8'))
        # Send one HTTP header line into socket
        # Fill in start
        '''Access the HTML file, and send one header line'''
        with open('HelloWorld.html') as html_file:
            source = html_file.read()
            html = HTML(html=source)
        ans = html.find('h1')
        connectionSocket.send(bytes(ans, 'utf-8'))
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        '''Create a text variable, then send the error message with 'utf-8' encoding'''
        text = "Error - Tile not found!"
        connectionSocket.send(bytes(text, "utf-8"))
        connectionSocket.close()
        # Fill in end
# Close client socket
# Fill in start
    '''Closing the Server socket (connectionSocket already closed)'''
    serverSocket.close()
# Fill in end
    sys.exit()  # Terminate the program after sending the corresponding
