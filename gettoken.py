import requests
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("Enter your username: ")
password = getpass ("Enter your password: ")

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
