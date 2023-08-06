#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys
import textwrap
import socketserver
import string
import readline
import threading
from time import *

import getpass
import os
import subprocess
import open_door

username = long_to_bytes(29099066774615156)  # garrett
password = long_to_bytes(7163082334141771109)  # changeme


class Service(socketserver.BaseRequestHandler):

    def handle(self)
        self.send(b"A port has opened... Look up")
		sleep(2)
        self.send(b"Just kidding. You think I would play the same tricks that many times?")
        sleep(1)
        self.send(b"Bye Bye!")

    def send(self, string, newline=True):
        if newline:
            string = string + b"\n"
        self.request.sendall(string)

    def receive(self, prompt=b"> "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()


class ThreadedService(
		socketserver.ThreadingMixIn,
		socketserver.TCPServer,
		socketserver.DatagramRequestHandler,
):
	pass


def main():
    print("Starting server...")
    port = 4321
    host = "0.0.0.0"

    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print("Server started on " + str(server.server_address) + "!")

    while True:
        sleep(10)


if __name__ == "__main__":
    main()
