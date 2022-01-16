import os
import pyautogui 
import time
import pyperclip
from pynput.keyboard import Key, Controller
keyboard = Controller()

dir = "C:\\Users\\User_Name\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\discord"
#replace dir with path of the discord exe or shortcut file
os.startfile(dir)
os.system(dir)

time.sleep(5)

#print(pyautogui.size())    
print(pyautogui.position())
#for your own keep your mouse at the text box and then run the program. The position should be printed. Change it in the next line.
pyautogui.click(x=891, y=1028) 

time.sleep(5)

n = 5
while n != 0:
    pyperclip.copy('pls beg')
    pyperclip.paste()
    pyautogui.click(x=891, y=1028) 
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    pyperclip.copy('pls hunt')
    pyperclip.paste()
    pyautogui.click(x=891, y=1028) 
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    pyperclip.copy('pls fish')
    pyperclip.paste()
    pyautogui.click(x=891, y=1028) 
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    pyperclip.copy('pls dig')
    pyperclip.paste()
    pyautogui.click(x=891, y=1028) 
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    pyperclip.copy('pls dep all')
    pyperclip.paste()
    pyautogui.click(x=891, y=1028) 
    with keyboard.pressed(Key.ctrl.value):
        keyboard.press('v')
        keyboard.release('v')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(5)

    pyautogui.click(x=616, y=968) 

    time.sleep(30)



#Size(width=1920, height=1080)
#Point(x=891, y=1028)
#Point(x=616, y=968)
