import socket
import sys

try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", port))

while True:
    try:
        response = client_socket.recv(4096).decode()
    except ConnectionAbortedError:
        print("Connection closed by host.")
        break

    # Note: I had to add this block of code to make my script
    # function like the one in the video. Since the server sends
    # "Goodbye!" before quitting, client_socket.recv() on line 15
    # does not result in an error and the script then gets stuck
    # on the blocking input call on line 32.
    if response == "OK! Goodbye!\n":
        client_socket.close()
        print("Connection closed by host.")
        break

    print(response)

    my_message = input("> ").encode('utf-8') + b'\n'
    client_socket.sendall(my_message)
