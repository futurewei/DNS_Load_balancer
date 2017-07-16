import socket
import time


# server to be our local
host = '127.0.0.1'
port =8000



#Create a new socket using the given address family, socket type and protocol number
s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Bind the socket to address. The socket must not already be bound.
s.bind((host, port))



#In non-blocking mode, if a recv() call doesn’t find any data,
# or if a send() call can’t immediately dispose of the data, an error exception is raised; 
s.setblocking(0) # set non-blocking.

quitting = False
print ("Sever Started.")

while not quitting:
	try:
		data, addr = s.recvfrom(2024) #buffer =1024
		#如果有
		if "Quit" in str(data):
			quitting = true

		#显示收到信息的时间，address. 信息是什么。
		strList = str(data).split()
		Request = ''
		for i in range(len(strList)):
			if i!=0 and i!=1:
				Request = Request + strList[i]+" "
		print (time.ctime(time.time()) + " sender: "+ strList[1]+ '. Request: '+ Request)
		print ("server 8000 process the Request")
	except:
		pass
s.close()

