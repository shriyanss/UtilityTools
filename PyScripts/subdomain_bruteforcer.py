import sys
try:
  target = sys.argv[1]
  wordlist = sys.argv[2]
except:
  print("Usage: python3 subdomain_bruteforcer.py <target> <path_to_wordlist>")
  sys.exit()
import socket

with open(wordlist, 'r') as file:
    for line in file:
        line = line.replace("\n", "")
        try:
            host = line + '.' + target
            ip = socket.gethostbyname(host)
            print(host)
        except:
            pass
