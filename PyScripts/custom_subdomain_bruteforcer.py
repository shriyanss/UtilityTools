import sys
try:
  main_url = sys.argv[1]
  target_host = sys.argv[2]
  protocol_prefix = sys.argv[3]
  port_suffix = sys.argv[4]
  wordlist = sys.argv[5]
except:
  print("Usage: python3 custom_subdomain_bruteforcer.py <main_url> <target_host> <protcol_prefix> <port_suffix> <wordlist>")
  sys.exit()

import requests

main_text = (requests.get(main_url)).text

with open(wordlist, 'r') as file:
  for line in file:
    line = line.replace("\n", '')
    url = protocol_prefix + "://" + line + "." + target_host + ":" + port_suffix + "/"
    try:
      txt = (requests.get(url)).text
      if txt == main_text:
        pass
      else:
        print(url)
    except:
      pass
