#!/usr/bin/python

from __future__ import print_function, unicode_literals

import SocketServer
import threading
import time

import db

class ScoreboardTCPHandler(SocketServer.StreamRequestHandler):
  def process(self, req):
    req = req.split(' ')
    if len(req) != 3:
        self.wfile.write('Wrong format! Should be: <user> <task> <flag>\n')
        return

    user = req[0][:8]
    task = req[1]
    flag = req[2]

    res = db.try_solve_task(user, task, flag)
    self.wfile.write(res + '\n')

  def handle(self):
    try:
      for line in self.rfile:
        line = line.rstrip()
        self.process(line)
    except:
      self.wfile.write('Oops!\n')
      raise

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
  pass

server = None
server_thread = None

def start_tcp_server(port):
  global server, server_thread
  server = ThreadedTCPServer(('', port), ScoreboardTCPHandler)
  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.start()

def stop_tcp_server():
  server.shutdown()
  server_thread.join()

def run_tcp():
  start_tcp_server(9999)
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    stop_tcp_server()

if __name__ == '__main__':
  run_tcp()
