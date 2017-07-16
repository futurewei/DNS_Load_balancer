# DNS_Load_balancer

During the internship, I got to play around with AWS EC2 where I found the Elastic Load Balancing to be very interesting. After some research about what Load balancing does and how Load Balancing DNS works, I decided to implement a homemade version for fun.
The Load balance  I did is Round Robin Algorithm and I used socket.io + python to implement it. 


Below is the initial stage where I lauched two servers on top. One load balancer Domain name server on left bottom. One client server to be called on right bottom
![742cc188-8ac3-4323-8920-4d4912c6e165](https://user-images.githubusercontent.com/13871858/28246397-c5392b74-69cd-11e7-91af-2155c8116790.png)




Upon called the client.py, we just made a domain request to load balancer DNS. In our case, it sends the 'www.test.com' to DNS port.
After confirming there's a IP mapping with the input Domain name, load balancer first direct this client to server1, which is at port 5000.  
Server1 outputs the information it got, which includes time, sender IP, and request message. In real development, if there's a database connected, server1 would be able to actually process the request from client.


![1fdb1b55-f269-48af-bb41-e199d47f94cb](https://user-images.githubusercontent.com/13871858/28246399-c8ef4618-69cd-11e7-8287-fdd94087700a.png)






now 
![7e4a6280-a5d1-4055-b072-459b3f2bbc77](https://user-images.githubusercontent.com/13871858/28246401-cc5475b2-69cd-11e7-9f2c-ba42df780d51.png)
