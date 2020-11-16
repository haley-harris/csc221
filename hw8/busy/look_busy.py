#! python3
# nudges mouse every 10 seconds to keep your online status in
# messaging apps from appearing idle

import pyautogui, time

pyautogui.FAILSAFE = True
starting_position = (1423, 820)

print('Starting program - press CTRL-C to quit')

# set mouse at bottom right corner of the screen
pyautogui.moveTo(starting_position)

try:
    while True:
        # move mouse to the left of starting position every 10 secs
        pyautogui.move(-5, 0, duration=0.25)
        time.sleep(10)
except KeyboardInterrupt:
    print(' program stopped')