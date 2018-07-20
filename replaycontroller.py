# can control the sc2 replay window, obsolete with current replay overlay

import win32ui
import win32gui
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
fullscreen = False

while True:
	if WindowExists("StarCraft II"):
		if not (start):
			handle = win32gui.FindWindow(0, "StarCraft II")
			win32gui.BringWindowToTop(handle)
			win32gui.SetForegroundWindow(handle)
			start = time.time()
		
		now = time.time()
		timer = int(now - start)
		if ((timer > 10) and (fullscreen == False)):
			keyboard.press_and_release('alt+enter')
			fullscreen = True
		
		if ((timer > 30) and (sendcommands == False)):
			keyboard.press_and_release('d')
			sendcommands = True
	else:
		start = 0
		sendcommands = False
		fullscreen = False
