#! python3
# draws spiral square on artboards

# add button='left' as drag argument to avoid errors on MacOS


import pyautogui, time

time.sleep(5)

pyautogui.click()

distance = 300
change = 20

while distance > 0:
    # move right
    pyautogui.drag(distance, 0, duration=0.2, button='left')
    distance = distance - change
    # move down
    pyautogui.drag(0, distance, duration=0.2, button='left')
    # move left
    pyautogui.drag(-distance, 0, duration=0.2, button='left')
    distance = distance - change
    # move up
    pyautogui.drag(0, -distance, duration=0.2, button='left')
    