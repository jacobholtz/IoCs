import requests
import json
import subprocess

# Open file to write
f = open("lockbit_sha256_hashes", "w")  

def malwarebazaar():
    f.write("##### Malware Bazaar #####\n")

    data = {
        'query': 'get_siginfo',
        'signature': 'lockbit',
    }

    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=15)
    json_response = response.content.decode("utf-8", "ignore")

    hashDict = json.loads(json_response)

    for hashValue in hashDict['data']:
        hash = hashValue['sha256_hash']
        f.write(hash + "\n")

    # Close the file
    f.close()

def main():
    # Start the scans
    malwarebazaar()

    # Add and push to github
    subprocess.run(["git", "add", "lockbit_sha256_hashes"])
    subprocess.run(["git", "commit", "-m", "Update hashes"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    main()