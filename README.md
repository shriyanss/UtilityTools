# UtilityTools
Web hacking utility tools in one .ipynb

# Pro Tip: Run the jupyter notebook file in google colab for faster execution

# Usage
## Python Scripts
All the python scripts does the same things as .ipynb. Just the thing different is it's python script and it takes arguments via command line (params are same as the those in jupyter notebook)

## Subdomain Bruteforcer
`wordlist` : The URL to wordlist (default already set)<br>`target`: Domain of the target
<br><br>Some wordlists for subdomain bruteforce can be found [here](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)<br> Just copy the raw URL for desired wordlist and paste it below.<br> **This tool checks if the host (subdomain) have an IP or not. If yes, then there's chance that subdomain is live**

## Custom Subdomain Bruteforcer
`main_url`: The URL of the main web page<br>`target_host`: Hostname of the target<br>`protocol_prefix`: Protocol to use [http/https]<br>`port_suffix`: Port number to check<br>`wordlist`: URL of the wordlist<br><br>
This tool checks if the content is matching with the main domain or not. If it matches, it excludes it, and if not, it is printed

## Custom subdomain checker
`main_url`: This is the URL of main page to match the code with
`wordlist`: This is the list of URLs containing URLs of subdomain

## Mass file finder
`files`: enter the file to search at a list of domains/subdomains (comma seperated value, please)<br>`subdomainList`: Path to the file containing domains/subdomains (one line each)<br>`protocol`: Protocol to use (*http/https*)<br>`port`: Port to use (*1-65535*)<br>`timeoutSec`: Set timeout for each request

This tool helps you find some specific files in the targeted domain list. E.g. find .git in all subdomains of target.com

## Display IP addresses
`hostnames`: Path to file containing hostnames to resolve IP of (1 per line)

Print the ip address of all domains in list (useful to find host header injection, identifying proxy, etc.)
