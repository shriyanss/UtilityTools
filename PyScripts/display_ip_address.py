import socket, sys

hostnames = sys.argv[1]

with open(hostnames, 'r') as file:
  for line in file:
    line = line.replace("\n", '')
    ip = socket.gethostbyname(line)
    print(ip + ": " + line)
