import socket
import random
import base64
import time
import select

def encode_number(number):
    # Convert the number to bytes and encode in Base64
    number_bytes = str(number).encode()
    encoded_bytes = base64.b64encode(number_bytes)
    encoded_number = encoded_bytes.decode()
    return encoded_number

def generate_addition_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    encoded_num1 = encode_number(num1)
    encoded_num2 = encode_number(num2)
    return num1, num2, encoded_num1, encoded_num2, num1 + num2

def generate_subtraction_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    encoded_num1 = encode_number(num1)
    encoded_num2 = encode_number(num2)
    return num1, num2, encoded_num1, encoded_num2, num1 - num2

def generate_multiplication_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    encoded_num1 = encode_number(num1)
    encoded_num2 = encode_number(num2)
    return num1, num2, encoded_num1, encoded_num2, num1 * num2

def handle_client_connection(client_socket):
    # Generate the first addition problem
    num1, num2, encoded_num1, encoded_num2, expected_result = generate_addition_problem()
    problem = f"What is {encoded_num1} + {encoded_num2}?"
    client_socket.send(problem.encode())

    # Set a timeout of 3 seconds for receiving data
    client_socket.settimeout(3)

    # Wait for the client's response
    ready = select.select([client_socket], [], [], 3)
    if ready[0]:
        response = client_socket.recv(1024).decode().strip()

        if response == str(expected_result):
            # Generate the subtraction problem
            num1, num2, encoded_num1, encoded_num2, expected_result = generate_subtraction_problem()
            problem = f"What is {encoded_num1} - {encoded_num2}?"
            client_socket.send(problem.encode())

            # Wait for the client's response
            ready = select.select([client_socket], [], [], 3)
            if ready[0]:
                response = client_socket.recv(1024).decode().strip()

                if response == str(expected_result):
                    # Generate the multiplication problem
                    num1, num2, encoded_num1, encoded_num2, expected_result = generate_multiplication_problem()
                    problem = f"What is {encoded_num1} * {encoded_num2}?"
                    client_socket.send(problem.encode())

                    # Wait for the client's response
                    ready = select.select([client_socket], [], [], 3)
                    if ready[0]:
                        response = client_socket.recv(1024).decode().strip()

                        if response == str(expected_result):
                            client_socket.send("sc{math_1S_bas1c}".encode())
                        else:
                            client_socket.send("Wrong answer".encode())
                    else:
                        client_socket.send("\nToo Late".encode())
                else:
                    client_socket.send("Wrong answer".encode())
            else:
                client_socket.send("\nToo Late".encode())
        else:
            client_socket.send("Wrong answer".encode())
    else:
        client_socket.send("\nToo Late".encode())

    # Close the connection
    client_socket.close()

def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Allow reuse of the address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a new connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        # Handle the client's request in a separate thread
        handle_client_connection(client_socket)

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 9902
    start_server(host, port)
