import requests
import json
import re
import sys
import time

def find_subdomains(domain_name, complite, file_name):
    headers = {
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'X-Requested-With': 'id.chie.subdomainfinder',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'crt.sh',
        'Referer': 'https://crt.sh/?q=[]&output=json',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S9210 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.74 Mobile Safari/537.36',
    }
    with requests.Session() as session:
        session.headers.update(
            headers
        )
        if bool(complite) != True:
            response = session.get('https://crt.sh/?q={}&output=json&exclude=expired'.format(domain_name), verify=True)
        else:
            response = session.get('https://crt.sh/?q={}&output=json'.format(domain_name), verify=True)

        x_data = json.loads(response.text)
        subdomains = set()
        for entry in x_data:
            subdomains.update(entry['name_value'].split('\n'))

        number = 0
        for subdomain in subdomains:
            open(f'{file_name}', 'a+').write(f'{subdomain}\n')
            number += 1
            print(f"\x1b[1;92m{number}\x1b[1;97m.\x1b[1;97m {subdomain}")
        return ("null")

if __name__ == "__main__":
    print("""\x1b[1;93m  ____        _     _____ _           _           
\x1b[1;93m / ___| _   _| |__ |  ___(_)_ __   __| | ___ _ __ 
\x1b[1;93m \___ \| | | | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
\x1b[1;93m  ___) | |_| | |_) |  _| | | | | | (_| |  __/ |   
\x1b[1;93m |____/ \__,_|_.__/|_|   |_|_| |_|\__,_|\___|_|   
\x1b[1;97m""")

    domain_name = input("\x1b[1;97mDomain (Ex:\x1b[1;92m facebook.com\x1b[1;97m):\x1b[1;92m ").lower()

    if re.match(r'^(?!https?:\/\/|www\.|.*[^a-zA-Z0-9.-]).+(\.[a-zA-Z]{2,})+$', domain_name):
        file_name = input("\x1b[1;97mFiles (\x1b[1;97mEx:\x1b[1;93m Temporary/Save.txt\x1b[1;97m):\x1b[1;92m ")
        type_ = input("\x1b[1;97mType (\x1b[1;91mQuick\x1b[1;97m/\x1b[1;92mComplite\x1b[1;97m):\x1b[1;92m ")

        with open(f'{file_name}', 'w+') as save:
            save.write("")
        save.close()

        print(f"\x1b[1;97mLooking for {domain_name}", end="", flush=True)
        for i in range(3):
            for dots in range(1, 4):
                print(f"\r\x1b[1;97mLooking for {domain_name}{'.' * dots}", end="", flush=True)
                time.sleep(0.5)
        print("\r                                        ")

        complite = False if type_.capitalize() == 'Quick' else True
        find_subdomains(domain_name, complite, file_name)

        print("\n\x1b[1;97mSuccessfully Saved Subdomain!")
        print(f"\x1b[1;97mDomain Count:\x1b[1;92m {len(open(file_name, 'r').readlines())}")
        print(f"\x1b[1;97mSaved in:\x1b[1;91m {file_name}")
        sys.exit(1)
    else:
        print("\n\x1b[1;91mInvalid Domain Name!")
        sys.exit(1)