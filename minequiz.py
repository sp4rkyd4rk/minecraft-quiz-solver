import os
import time
import subprocess
import platform
import pyperclip
import re

regexp = r"\d+ \+ \d+"
patt = re.compile(regexp)


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

        #if "[main/INFO]: [CHAT] Поздравляем" or "[main/INFO]: [CHAT] выйграл" not in line:
        #    continue
            

