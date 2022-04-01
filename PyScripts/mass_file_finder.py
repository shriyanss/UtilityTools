import requests, socket, sys

try:
    files = sys.argv[1]
    subdomainList = sys.argv[2]
    protocol = sys.argv[3]
    port = int(sys.argv[4])
    timeoutSec = int(sys.argv[5])
except:
    print("Usage: python3 mass_file_finder.py <files> <subdomainList> <protocol> <port> <timeoutSec>")

fileArray = files.split(",")
file = open(subdomainList, 'r')

for fl in fileArray:
  for line in file:
      line = line.replace("\n", '')
      url = protocol + "://" + line + ":" + str(port) + "/" + fl
      try:
        ip = socket.gethostbyname(line)
        rqst = requests.get(url, timeout=timeoutSec)
        if rqst.status_code != 404:
          print(url)
          print(rqst.status_code)
      except:
        pass
