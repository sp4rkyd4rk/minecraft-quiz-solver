import os
import time
import subprocess
import platform
import re

import pyperclip
import keyboard

regexp = r"\d+ \+ \d+"
patt = re.compile(regexp)

enter_sequence = 'ctrl+v, enter'

if platform.system() == 'Darwin':
    logfile = open(os.path.expanduser("~/Library/Application Support/minecraft/logs/latest.log"), "r", encoding="utf-8")
elif platform.system() == 'Windows':
    logfile = open(os.getenv("APPDATA") + "/.minecraft/logs/latest.log", "r")
else:
    logfile = open(os.path.expanduser("~/.minecraft/logs/latest.log"), "r", encoding="utf-8")


def scroll_logs(logfile):
  logfile.seek(0,2)
  while True:
    line = logfile.readline()
    if not line: 
        time.sleep(0.1)
        continue
    yield line



if __name__ == "__main__":
    lines = scroll_logs(logfile)
    for line in lines:
        if re.search(patt, line):
                arr = line.split(" ")
                solution = int(arr[7]) + int(arr[9])
                print(solution)
                pyperclip.copy(solution)


                if platform.system() == 'Darwin':
                    keyboard.press_and_release('t')
                    time.sleep(0.25)
                    keyboard.press_and_release('cmd+v, enter')
                    pyperclip.copy(solution)
                else:
                    keyboard.press_and_release('t')
                    time.sleep(0.25)
                    keyboard.press_and_release(enter_sequence)
                    pyperclip.copy(solution)



