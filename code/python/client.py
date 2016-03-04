import sys
import socket

s = socket.socket()
s.connect(("10.10.10.137", 80))
s.send(str(sys.argv[1]))
s.close()
