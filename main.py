import pyperclip
import time
import keyboard
import pyautogui
import random
import string

from butterfingers import butterfinger

with open("wordlist.txt", "r") as f:
    content = f.readlines()

used = []
letters = ""
found = "6969"

def activate():
    global letters, used, found

    while 1:
        x,y = pyautogui.position()
        pyautogui.moveTo(808, 570) # Change this depending on where the bomb text is on your screen.
        pyautogui.leftClick()
        pyautogui.leftClick()
        before = pyperclip.paste()
        keyboard.send("ctrl+c")
        time.sleep(0.1)

        result = pyperclip.paste()
        time.sleep(0.01)
        pyperclip.copy(before)

        pyautogui.moveTo(x,y)
        pyautogui.leftClick()

        search = result.upper().strip()
        found = ["6969"]
        top = 0
        shortest = 696969
        for i in content:
            if search in i and i not in used:
                test=letters+i
                not_good = False
                for x in string.ascii_uppercase:
                    if x not in test:
                        not_good = True
                        break
                if not not_good:
                    found = [i]
                    break

                amount = 0
                for x in i:
                    if x not in letters:
                        amount+=1
                if amount > top:
                    found = [i]
                    top = amount
                    shortest = len(i)
                elif amount == top and len(i) < shortest:
                    found = [i]
                    top = amount
                    shortest = len(i)
                elif amount+4 >= top and len(i)+4 < shortest:
                    found = [i]
                    top = amount+4
                    shortest = len(i)
                elif amount == top and len(i) == shortest:
                    found.append(i)

        if found == ["6969"]:
            print("Did not find any available matches.")
            used = []
            continue

        found = random.choice(found)

        used.append(found)
        butterfinger(found)
        keyboard.press_and_release('enter')

        time.sleep(0.2)
        try:
            if pyautogui.pixelMatchesColor(566, 1004, (49, 43, 38), tolerance=5): # Change this depending on where the input text box is on your screen
                break
        except:pass

    letters+=found

    for i in string.ascii_uppercase:
        if i not in letters:
            return

    letters = ""
    used = []

print("READY!")
while 1:
    try:
        if pyautogui.pixelMatchesColor(788, 1002, (25, 21, 19), tolerance=5): # Change this depending on where the input text box is on your screen
            time.sleep(random.randint(1,100)/70)
            activate()
    except:
        continue
    time.sleep(0.15)
