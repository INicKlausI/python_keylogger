import socket
import os
import platform

def open_server():
	while True:
		connect, client = tcp.accept()
		print ('connectnect by', client)
		while True:
			menssage = connect.recv(1024)
			if not menssage: break
			file = open(logfile, "a")
			file.write(menssage.decode())
			print (client, menssage)
		connect.close()	

if __name__ == '__main__':
	if (platform.system() == 'Linux'):
		clearCommand = 'clear'
	elif (platform.system() == 'Windows'):
		clearCommand = 'cls'
	os.system(clearCommand)
	HOST = '127.0.0.1'
	PORT = 5050
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ORIGIN = (HOST, PORT)
	tcp.bind(ORIGIN)
	tcp.listen(1)
	logfile = 'server_log.txt'
	open_server()
