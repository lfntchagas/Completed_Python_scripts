import requests
import json
import hashlib

url = ""
prompt = "\nType the application name to be converted to MD5\n"


def passwdstate():
    payload = {
        "PasswordListID": "970", 
        "Title": my_string, 
        "UserName": ticket, 
        "password": hash_value,
        "APIKey": "",
        "Description": web_site
        }
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "172",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
            }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    print(response.text)


def getHash256(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()


def getmd5(string):
    hash_object = hashlib.md5(string.encode())
    return hash_object.hexdigest()




web_site = input("\nWhat is the website you are generating this Bot Whitelist?\n").lower()
ticket = input("\nWhat is the JIRA-ticket number?\n").upper()
my_string = input(prompt).lower() + '_' + ticket.lower()

print(my_string)

hash_value = 'X-Akamai-Bot-Allow: ' + getmd5(string=my_string)

print(f"\nHere below is the hash-value for the application {my_string}")
print(f"\n{hash_value}\n")
passwdstate()
