# Import socket library
from socket import *

# Import sys package if you want to terminate the program
import sys

# Nick Janota
# CSC 138
# Assignment 2
# Due 10/23/25

def create_server_socket(port):
    # Prepare a server socket
    # Fill in start

    # AF_INET indicates ipv 4
    # sock_stream indicates TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # bind the socket to port
    # arg1 binds the socket to specific ipa -
    # in this case '' binds server to all available networks interfaces
    # ar2 is the port you want to bind to
    serverSocket.bind(('', port))
    # start listening for incoming client connections - 1 connection in queue at a time
    serverSocket.listen(1)
    # Fill in end


    print(f"The server is ready to receive on port: {port}")
    return serverSocket

def handle_request(connectionSocket):
    try:
        # Receive the HTTP request
        # This can read up to 2048 Bytes and decode into a string
        message = connectionSocket.recv(2048).decode()

        # If nothing was sent by the client then we should close the connection
        if not message:
            connectionSocket.close()
            return
        
        # Prepare HTTP response header
        # Fill in start
        # Build the HTTP/1.1 200 OK Header
        response_header = "HTTP/1.1 200 OK\r\n"
        # Append content type and newline with carriage return
        response_header += "Content-Type: text/html\r\n"
        # Required by HTTP >> separates header from body
        response_header += "\r\n"
        # Fill in end

        # Get the requested file from the message
        # This removed leading /: Uses string indexing
        # Example: the request line >> GET /index.html HTTP/1.1
            # split()[1] >> /index.html, [1:] >> index.html
        filename = message.split()[1][1:]

        # Open the requested file and get the HTML body content
        # Fill in start
        # Open the file in Binary-Mode and handle file bytes
        # Since decode returns bytes this can concat with the header and sent to sendall
        with open(filename, 'rb') as f:
            response_body = f.read()
        # Fill in end

        # Send response message
        # Fill in start
        # Send [headerBytes, bodyBytes] concatenated 
        connectionSocket.sendall(response_header.encode() + response_body)
        # Fill in end

        # Close the socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

        # Terminate the program after sending the corresponding data
        # Comment it out if you want the server to be always ON
        #sys.exit()


    except IOError:
        # Prepare 404 Not Found HTTP header
        # Fill in start
        # Handle on 404 Error
        response_header = "HTTP/1.1 404 Not Found\r\n"
        response_header += "Content-Type: text/html\r\n"
        response_header += "\r\n"
        # Fill in end

        # Prepare the HTML body content of 404 Not Found page
        # Fill in start
        response_body = b"<html><head></head><body><h1>404 Not Found</h1></body></html>"
        # Fill in end

        # Send response message
        # Fill in start
        # Same concept as 200 OK >> send as bytes and concatenate
        connectionSocket.sendall(response_header.encode() + response_body)
        # Fill in end

        # Close socket
        # Fill in start
        connectionSocket.close()
        # Fill in end


if __name__ == "__main__":
    port = 12000
    serverSocket = create_server_socket(port)
    while True:
        connectionSocket, addr = serverSocket.accept()
        handle_request(connectionSocket)
