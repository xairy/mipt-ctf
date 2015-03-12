#!/usr/bin/env python
import os
from Crypto.PublicKey import RSA
import SocketServer
import threading
import time

flag = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

class threadedserver(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class incoming(SocketServer.BaseRequestHandler):
  def handle(self):
    cur_thread = threading.current_thread()
    welcome = """
*******************************************
***             Welcome to the          ***
***    FlAg EnCrYpTiOn SeRviCe 9000!    ***
*******************************************

We encrypt the flags, you get the points!
"""
    self.request.send(welcome)
    rsa = RSA.generate(1024,os.urandom)
    n = getattr(rsa,'n')

    #no one will ever be able to solve our super challenge!
    self.request.send("To prove how secure our service is ")
    self.request.send("here is an encrypted flag:\n")
    self.request.send("==================================\n")
    self.request.send(hex(pow(int(flag.encode("hex"), 16),3,n)))
    self.request.send("\n==================================\n")
    self.request.send("Find the plaintext and we'll give you points\n\n")
    
    while True:
      self.request.send("\nNow enter a message you wish to encrypt: ")
      m = self.request.recv(1024)
      self.request.send("Your super unreadable ciphertext is:\n")
      self.request.send("==================================\n")
      self.request.send(hex(pow(int(m.encode("hex"), 16),3,n))) 
      self.request.send("\n==================================\n")

server = threadedserver(("0.0.0.0", 6666), incoming)
server.timeout = 4
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

server_thread.join()
