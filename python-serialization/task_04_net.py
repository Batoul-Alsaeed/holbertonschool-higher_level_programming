#!/usr/bin/env python3
import socket
import json

def start_server(host='127.0.0.1', port=65432):
    """Start a server that listens for one dictionary from a client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server listening on", host, ":", port)

        conn, addr = server_socket.accept()
        with conn:
            print("Connected by", addr)
            data = conn.recv(4096)
            if not data:
                return
            try:
                received_dict = json.loads(data.decode())
                print("Received Dictionary from Client:")
                print(received_dict)
            except Exception as e:
                print("Failed to deserialize:", e)

def send_data(dictionary, host='127.0.0.1', port=65432):
    """Client function to send a dictionary to the server."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            json_data = json.dumps(dictionary)
            client_socket.sendall(json_data.encode())
    except Exception as e:
        print("Connection failed:", e)
