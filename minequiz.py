import os
import time
import subprocess

# strings = ['[23:16:29]', '[main/INFO]:', '[CHAT]', 'Чат-игра', '»', 'Решите', 'пример:', '676', '+', '898', 'кто', 'первый', 'решит', 'пример,', 'получит:', '30$\n']

def scroll_logs(logfile):
  logfile.seek(0,2)
  while True:
    line = logfile.readline()
    if not line: 
      time.sleep(0.1)
      continue
    yield line


if __name__ == "__main__":
  logfile = open("/Users/sp4rkyd4rk/Library/Application Support/minecraft/logs/latest.log", "r")
  lines = scroll_logs(logfile)
  for line in lines:
    if "[main/INFO]: [CHAT] Чат-игра" in line:
    	arr = line.split(" ")
    	solution = int(arr[7]) + int(arr[9])
    	print(solution)
    	subprocess.run("pbcopy", universal_newlines=True, input=str(solution))