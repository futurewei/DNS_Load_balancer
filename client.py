
import socket
import threading
import time


#Once a thread has acquired it, subsequent attempts to
# acquire it block, until it is released; any thread may release it.
shutdown = False


host = '127.0.0.1'
port = 9000

server = ('127.0.0.1', 2000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

domain = 'www.test.com '
sender = host +','+ str(port)+ ' '
HTTP_request = domain + sender + "Hello~"
s.sendto(HTTP_request.encode(), server)
print ('sent')
shudown = True
s.close()