import socket
import time
import threading


# server to be our local
host = '127.0.0.1'
port =2000
DNS_port_list = [('127.0.0.1',5000), ('127.0.0.1',8000)]
domain = 'www.test.com'


#Create a new socket using the given address family, socket type and protocol number
s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Bind the socket to address. The socket must not already be bound.
s.bind((host, port))
tLock = threading.Lock()


#In non-blocking mode, if a recv() call doesn’t find any data,
# or if a send() call can’t immediately dispose of the data, an error exception is raised; 
s.setblocking(0) # set non-blocking.
IP = 0
quitting = False
print ("DNS Sever Started.")
data = '*'
while not quitting:
	try:
		data, addr = s.recvfrom(2024) #buffer =1024
		print (data)
		if data != '*':
			val = str(data).split()[0][2:]
			if val == 'www.test.com':
				s.sendto(data, DNS_port_list[IP])
				tLock.acquire()
				IP = (IP +1) % len(DNS_port_list)
				data = '*'
				tLock.release()
			else:
				print ('Incorrect Domain Name')
	except:
		pass
s.close()