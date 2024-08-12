import requests
import json

# Open file to write
f = open("LockBit_sha256_hashes", "w")

data = {
    'query': 'get_siginfo',
    'signature': 'lockbit',
}

response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=15)
json_response = response.content.decode("utf-8", "ignore")

hashDict = json.loads(json_response)

for hashValue in hashDict['data']:
    hash = hashValue['sha256_hash']
    f.write(hash)

# Close the file
f.close()