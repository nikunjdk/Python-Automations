#! python3
# Automatic Wifi Connector bot 

import os, sys

saved_profiles = os.popen('netsh wlan show profiles').read()

available_profiles = os.popen('netsh wlan show networks').read()
print('Available Profiles: ')
print(available_profiles)

while True:
	preferred_ssid = input('Enter the preferred SSID for your connection: ')
	if preferred_ssid in saved_profiles and available_profiles:
		os.popen('netsh wlan disconnect')
		print('-----Connecting-----')
		resp = os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
		print(resp)
		break
	elif preferred_ssid in available_profiles:
		print("SSID not saved, Please try again")
	else:
		print("Incorrect SSID, Please try again")