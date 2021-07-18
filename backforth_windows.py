import pyautogui
import time
import keyboard

while True:
    # pyautogui.press(['w']*500)
    # pyautogui.press(['s']*500)

    for i in range(100):
        keyboard.press('w')
        keyboard.release('w')
    for j in range(100):
        keyboard.press('s')
        keyboard.release('s')
    time.sleep(10)