# Step 1: Initialize empty project structure
import socket      #  For network communication
import threading   #  For handling multiple clients via threads
import time        #  For timing and periodic statistics}
# ✅ Step 2: Create a basic TCP server
# This is the most basic server: it waits for a client and sends a message backS
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #  Create a TCP socket for communication
    server_socket.bind(("", port))  #  Link the socket to a port so it knows where to listen
    server_socket.listen()  #  Start waiting for client connections
    print(f"[STARTED] Server is running on port: {port}")

    while True:
        client_socket, address = server_socket.accept()  # Accept a new client connection
        print(f"[CONNECTED] Client connected from: {address}")
        client_socket.sendall("Server connected\n".encode())  #  Send a message back to the client
        client_socket.close()  # Close the connection

#  Main entry: this runs the server
if __name__ == "__main__":
    default_port = 51234  #  Default port number (can be changed)
    start_server(default_port)
