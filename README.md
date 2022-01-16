# DiscordDankMemerBot
Python bot to automatically type in commands and grind money for you in the Dank Memer discord bot.

DankMemer is a discord bot. This program is written for you to grind money and make money. Turn it on in the night and go it sleep ez money. Efficiency is low and making good decent money takes time. Will put up a 2.0 version soon enough.

List of neccessary packages:
os
pyautogui
time
pyperclip
pynput


What the program does is that first it open the discord application and then clicks on the text box using pyautogui. Then starts entering text using pyperclip.

The program is set as per screen size of 1920,1080 which givs problems when screen size is different as the position of the text box changes.However you can find your own using the print(pyautogui.position()) by just keeping the cursor at the text box and running the program.
