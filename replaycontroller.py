# can control the sc2 replay window, obsolete with current replay overlay

import win32ui
import keyboard
import time

def WindowExists(classname):
    try:
        win32ui.FindWindow(classname, None)
    except win32ui.error:
        return False
    else:
        return True

start = 0
sendcommands = False

while True:
	if WindowExists("StarCraft II"):
		if not (start):
			start = time.time()
		
		now = time.time()
		timer = int(now - start)

		if ((timer > 30) and (sendcommands == False)):
			# lower the time-bar
			keyboard.press_and_release('control+t')
			time.sleep(0.2)
			# show the APM overlay
			keyboard.press_and_release('control+c')
			sendcommands = True
	else:
		start = 0
		sendcommands = False
