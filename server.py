

"""

	Author : 3x1t1um

"""

import socket
from cryptography.fernet import Fernet
import base64


def init():

	socket.bind(('', 1550))
	socket.listen(5)

	print('Waiting for connexion...')

	client, address = socket.accept()

	print("{} connected".format(address))
	print('Generate key...')

	key = Fernet.generate_key()

	print('Done')
	print('Saving key with base64...')

	with open('key_for_'+str(address)+'.txt', 'w') as f:
		f.write(base64.b64encode(key).decode('utf-8'))
	f.close()

	print('Done')
	print('Sending key...')

	client.send(base64.b64encode(key))

	print('Done')


if __name__ == '__main__':
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	init()
