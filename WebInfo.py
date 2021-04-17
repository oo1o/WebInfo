import requests
import socket
import re
import sys
import os
import time

while True:
	A = '\033[1;10m'
	B = '\033[1;30m'
	C ='\033[1;36m'
	D =('='*50)
	banner = (f"""{A}{D}
	<>---<>---<>---<>---<>---<>---<>---<>---<>
		[*] Web information [*]  
	<>---<>---<>---<>---<>---<>---<>---<>---<>        
		>> Naplon ◕_◕ <<
	_   _             _             
	| \ | |           | |            
	|  \| | __ _ _ __ | | ___  _ __  
	| . ` |/ _` | '_ \| |/ _ \| '_ \ 
	| |\  | (_| | |_) | | (_) | | | |{C}
	|_| \_|\__,_| .__/|_|\___/|_| |_|
				| | instagram: 3h6h                 
				|_| Telegram: naplon0
					
	<>---<>---<>---<>---<>---<>---<>---<> 

	<>---<>---<>---<>---<>---<>---<>---<>    
	""") 

	print(banner)

	print('''
	1)Fetching the IP address of the site
	2)Read data for the site
	3)Determine the open port
	4)Find out hidden paths on the site
	5)Extracting tracks within the site 
	6)Subdomain Detector 
	7)Exit()
	''')
	
	user = input()

	os.system('CLS')
	

	if user == '1':
		
		print(banner)
		print("Fetching the IP address of the site")
		print('=' * 45)
		host = input('Enter the host name: ')
		ip = socket.gethostbyname(host)
		print('The ip address of '+ host + ' is:' + ip)

	elif user == '2':
		print(banner)
		print("[Read data for the site]")
		print("=" * 45)
		print("//Link must contain http or https\\")
		print("=" * 45)
		link = input('Enter the link: ')
		url = ''+link+''
		print('•••••••••••••••••••••••••••••••••••')
		print("")
		data = requests.get(url).text
		print(data)
		print("")

	elif user == '3':
		print(banner)
		print("[Determine the open port]")
		print('=' * 45)
		ip = str(input("Enter the site's IP address: "))
		print('=' * 45)
		ports = [19,20,21,22,23,24,25,80,443]
		
		for p in ports:
			so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			so.settimeout(1)
			re = so.connect_ex((ip, p))
			if re == 0:
				server = socket.getservbyport(p)
				print("--> the port {} is open --> {}".format(p, server))
			so.close()

	else:
		print('')

	if user == '4':
		print(banner)
		print("[*] Find out hidden paths on the site [*]")
		print("=" * 45)
		print("[//Link must contain http or https\\]")
		print("=" * 45)
		user = str(input('Enter the link: '))
		domains = user +"/robots.txt"

		try:
			page = requests.get(domains,"html.parser").text
			hidden = re.findall("Disallow\: \S{1,}",page)

			for i in hidden:
				link = "[*]" + user + i[10:]
				print(link)
				fil = open("blacklink.txt", "a")
				fil.write("\n"+link)
				fil.close()
		except:
			pass

	else:
		print('')


	if user == '5':
		print(banner)
		print("[*]Extracting tracks within the site[*]")
		print("=" * 45)
		print("//Link must contain http or https\\")
		
		host = str(input("Enter the website link: "))
		file = input("File Name: ")
		fi = open(file, "r")
		re = fi.read()
		fire = re.splitlines()

		try:

			for word in fire:
				url = host + "/" + word
				req = requests.get(url)

				if req.status_code == 200:
					print("[*]>>Found : " + url)

		except:
			print("Exit..")
			sys.exit()
	else:
		print('')


	if user == '6':
		print(banner)
		print("=" * 45)
		print("[*]Subdomain Detector [*]")
		print("Example >>example.com")
		print("=" * 45)
		host = str(input("Enter the host name: "))
		file = input("File Name: ")
		f = open(file, "r")
		r = f.read()
		sublist = r.splitlines()
		for sub in sublist:
			domain = "http://" + sub + "." + host
			
			try:
				r = requests.get(domain, "http.parser")
				if r.status_code == 200:
					print("[*]You have discovered a subdomain : " + domain)

					fil = open("subsave.txt", "a")
					fil.write('\n'+domain)
					fil.close()
			except requests.ConnectionError:
				pass
			except KeyboardInterrupt:
				print("Exit..")
				sys.exit()



	if user == '7':
		print("Exit..")
		time.sleep(0.3)
		print("20%■■□□□□□□□□")
		time.sleep(0.3)
		print("30%■■■□□□□□□□")
		time.sleep(0.3)
		print("40%■■■■□□□□□□")
		time.sleep(0.3)
		print("50%■■■■■□□□□□")
		time.sleep(0.3)
		print("60%■■■■■■□□□□")
		time.sleep(0.3)
		print("70%■■■■■■■□□□")
		time.sleep(0.3)
		print("80%■■■■■■■■□□")
		time.sleep(0.3)
		print("90%■■■■■■■■■□")
		time.sleep(0.5)
		print("100%■■■■■■■■■")
		time.sleep(0.5) 
	sys.exit()
