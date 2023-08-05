import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    # Send banner message to the client
    banner_message = "sc{easyOne}"
    client_socket.send(banner_message.encode())

    # Close the connection after sending the banner
    client_socket.close()

# Function to start the server and listen for incoming connections
def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    # Set the host and port for the server
    HOST = '0.0.0.0'
    PORT = 9910

    # Start the server
    start_server(HOST, PORT)

