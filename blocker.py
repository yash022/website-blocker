import time
from datetime import datetime as dt

hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "0.0.0.0"
website_list =["www.instagram.com", "www.youtube.com","my.kodular.io" , "community.kodular.io" , "youtube.com" , "instagram.com" , "facebook.com ", "discord.com" ]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")

	if dt.now() > dt(dt.now().year, dt.now().month, dt.now().day,18):
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.truncate(0)
			file.close()
			print("Fun hours...")
			
	
	time.sleep(5)
