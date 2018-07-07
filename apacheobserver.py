import requests
import htmllistparse
import random
import urllib.request,urllib.error
import os
import glob

# You need to enable directory listing!
website = 'https://m1nd.io/Replays/'

script_path = os.path.dirname(os.path.abspath( __file__ ))
temp_path = (script_path + '\\temp\\')

if not os.path.exists(temp_path):
	os.makedirs(temp_path)


def startbattle():
	# get results from API
	cwd, listing = htmllistparse.fetch_listing(website, timeout=10)
	battle = random.choice(listing)
	print (battle.name)

	replayfile = str(website) + str(battle.name)
	replaysave = temp_path + str(battle.name)


	# download replay
	try:
		urllib.request.urlretrieve (replayfile, replaysave)
	except urllib.error.URLError as e:
		return


	# run Observer
	os.system("ExampleObserver.exe --Path \"" + replaysave + "\"")
	
	# delete temp files
	tempfilelist = glob.glob(os.path.join(temp_path, "*.*"))
	for tempfile in tempfilelist:
		os.remove(tempfile)

# Main Loop
while True:
	os.system('cls')
	startbattle()
