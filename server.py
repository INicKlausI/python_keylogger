import socket
import os
import platform

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
while True:
	con, cliente = tcp.accept()
	print ('Conectado por', cliente)
	while True:
		msg = con.recv(1024)
		if not msg: break
		arq = open(logfile, "a")
		arq.write(msg.decode())
		print (cliente, msg)
	con.close()