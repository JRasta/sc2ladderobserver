import requests
import json
import random
import urllib.request,urllib.error
import os
import glob

script_path = os.path.dirname(os.path.abspath( __file__ ))
temp_path = (script_path + '\\temp\\')

if not os.path.exists(temp_path):
	os.makedirs(temp_path)

website = 'http://107.161.27.148'
api = '/api/game_results'

def startbattle():
	# get results from API
	r = requests.get(website + api)
	r.text
	data = json.loads(r.text)
	battle = random.choice(data)

	# define a few vars for easier handling
	battleid = battle['id']
	map = battle['map']
	winner_name = battle['winner_name']
	replay = battle['replay']
	replayfile = str(website) + str(replay)
	replaysave = temp_path + str(battleid) + ".Sc2Replay"
	
	bot_1_authorname = battle['bots'][0]['author']
	bot_1_botname = battle['bots'][0]['name']
	bot_1_race = battle['bots'][0]['race']
	bot_1_match_count = battle['bots'][0]['match_count']
	bot_1_win_count = battle['bots'][0]['win_count']

	bot_2_authorname = battle['bots'][1]['author']
	bot_2_botname = battle['bots'][1]['name']
	bot_2_race = battle['bots'][1]['race']
	bot_2_match_count = battle['bots'][1]['match_count']
	bot_2_win_count = battle['bots'][1]['win_count']

	# download replay
	try:
		urllib.request.urlretrieve (replayfile, replaysave)
	except urllib.error.URLError as e:
		return

	# print replay data to CLI
	print("Round " + str(battleid))
	print("----------\n")
	print(bot_1_botname + " (" + bot_1_race + ") vs " + bot_2_botname + " (" + bot_2_race + ")")
	print("")
	print(bot_1_botname)
	print("Author: " + bot_1_authorname)
	print("Rounds/Wins: " + str(bot_1_match_count) + "/" + str(bot_1_win_count))
	print("")
	print("")
	print(bot_2_botname)
	print("Author: " + bot_2_authorname)
	print("Rounds/Wins: " + str(bot_2_match_count) + "/" + str(bot_2_win_count))
	print ("")
	print ("")

	# print replay data to files in temp so we can use them in OBS read-from-file-function
	print("Round-ID: " + str(battleid), file=open(script_path + "\\temp\\round.txt", "a"))
	print("Winner: " + str(winner_name), file=open(script_path + "\\temp\\winner.txt", "a"))

	print("AI: " + str(bot_1_botname), file=open(script_path + "\\temp\\bot_1.txt", "a"))
	print("Author: " + str(bot_1_authorname), file=open(script_path + "\\temp\\bot_1.txt", "a"))
	print(("Rounds/Wins: " + str(bot_1_match_count) + "/" + str(bot_1_win_count)), file=open(script_path + "\\temp\\bot_1.txt", "a"))
	
	print("AI: " + str(bot_2_botname), file=open(script_path + "\\temp\\bot_2.txt", "a"))
	print("Author: " + str(bot_2_authorname), file=open(script_path + "\\temp\\bot_2.txt", "a"))
	print(("Rounds/Wins: " + str(bot_2_match_count) + "/" + str(bot_2_win_count)), file=open(script_path + "\\temp\\bot_2.txt", "a"))

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
