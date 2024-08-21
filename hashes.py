"""
TODO:
For some reason samples submitted by anonymous accounts are skipped
Add ThreatFox implementation
"""

import requests, json, subprocess, sys


# APIs to pull hashes from
def malwarebazaar(sig):
    file = sig + "_sha256_hashes"
    # Open file to write
    f = open( file, "w")  
    f.write("##### " + sig + " hashes from Malware Bazaar #####\n")

    data = {
        'query': 'get_siginfo',
        'signature': sig,
        'limit': 1000
    }

    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=15)
    json_response = response.content.decode("utf-8", "ignore")

    hashDict = json.loads(json_response)

    try:
        for hashValue in hashDict['data']:
            hash = hashValue['sha256_hash']
            f.write("\n" + hash)
    except KeyError:
        print("Signature not found or valid")

    # Close the file
    f.close()

    # Add and push to github
    subprocess.run(["git", "add", file])
    subprocess.run(["git", "commit", "-m", "Update hashes"])
    subprocess.run(["git", "push"])

def main():
    try:
        sig = sys.argv[1]
    except IndexError:
        print("Usage: python hashes.py signature")
        sys.exit()

    # Start the scans
    malwarebazaar(sig)

if __name__ == "__main__":
    main()