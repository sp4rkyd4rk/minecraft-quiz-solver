import os
import time
import platform
import re
import pyperclip
import keyboard

addition_pattern = re.compile(r"(\d+) \+ (\d+)")

if platform.system() == 'Darwin':
    mc_log_path = os.path.expanduser("~/Library/Application Support/minecraft/logs/latest.log")
elif platform.system() == 'Windows':
    mc_log_path = os.getenv("APPDATA") + "/.minecraft/logs/latest.log"
else:
    mc_log_path = os.path.expanduser("~/.minecraft/logs/latest.log")


def scroll_logs(logfile):
    logfile.seek(0, 2)
    while True:
        line = logfile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def main():
    logfile = open(mc_log_path, "r", encoding='utf-8')
    lines = scroll_logs(logfile)
    for line in lines:
        add_match = addition_pattern.search(line)
        if add_match:
            a, b = add_match.groups()
            solution = int(a) + int(b)

            print(str(time.ctime()) + ": " + str(solution))
            pyperclip.copy(solution)

            keyboard.press_and_release('t')
            time.sleep(1)
            keyboard.press_and_release(
                'ctrl+v, enter'
            )
            pyperclip.copy(solution)


if __name__ == "__main__":
    main()
