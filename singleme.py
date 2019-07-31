import sys
import time
import socket
import thread

def isup(port=8989):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		return sock.connect_ex(("127.0.0.1", port))
	except:
		return 1 # connection refused
	finally:
		sock.close()

def crt_instnc(port=8989):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(("127.0.0.1", port))
		sock.listen(5)
		while 1:
			(client, (ip, port)) = sock.accept()
			client.close()
	finally:
		sock.close()

def singleme(port=8989):
	if not isup(): # if server is up before, it will prevent myself to run
		sys.exit()
	thread.start_new_thread(crt_instnc,(port,))

if __name__ == "__main__":
	# the default port is 8989, but you can change it by changing the port address. me = singleme(port=7070)
	me = singleme() # will sys.exit() if similar program is running
	while 1:
		time.sleep(1)
