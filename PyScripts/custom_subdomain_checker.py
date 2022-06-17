import sys
try:
  main_url = sys.argv[1]
  wordlist = sys.argv[2]
except:
  print("Usage: python3 custom_subdomain_checker.py <main_url> <wordlist>")
  sys.exit()

import requests

main_text = (requests.get(main_url)).text

with open(wordlist, 'r') as file:
  for line in file:
    line = line.replace("\n", '')
    try:
      txt = (requests.get(line)).text
      if txt == main_text:
        pass
      else:
        print(line)
    except:
      pass
