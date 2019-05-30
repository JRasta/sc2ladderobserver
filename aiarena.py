import requests
import json
import urllib.request, urllib.error
import os
import glob

script_path = os.path.dirname(os.path.abspath(__file__))
temp_path = (script_path + '\\temp\\')

if not os.path.exists(temp_path):
    os.makedirs(temp_path)

token = 'redacted'

already_visited = []


def startbattle():
    # get results from API
    r = requests.get('https://ai-arena.net/api/results/?ordering=-created', headers={'Authorization': "Token " + token})
    r.text
    data = json.loads(r.text)

    # results are ordered by match id from lowest to highest.
    # we always want to show the game with the highest id that
    # has not been shown already.
    # If there is no new games, reset.
    found_new_game = False
    for battle in reversed(data['results']):
        if battle['id'] not in already_visited:
            already_visited.append(battle['id'])
            found_new_game = True;
            break
    if not found_new_game:
        already_visited.clear()
        return

    # define a few vars for easier handling
    battleid = battle['id']
    winner = battle['winner']
    replayfile = str(battle['replay_file'])
    replaysave = temp_path + str(battleid) + ".Sc2Replay"

    # download replay
    try:
        urllib.request.urlretrieve(replayfile, replaysave)
    except urllib.error.URLError as e:
        return

    # print replay data to CLI
    print("Round " + str(battleid))
    print("----------\n")
    print("Winner: " + str(winner))

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
