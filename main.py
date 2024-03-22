import requests
import colorama
colorama.init(convert=True)
from colorama import Fore
import sys
sys.stdout.write("\x1b]2;Relationship data fetcher by 8c\x07")

token = input(Fore.MAGENTA + 'Enter your Discord token: ')

headers = {
    'authorization': token,
}

response = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)

if response.status_code == 200:
    print(Fore.MAGENTA + "fetched relationship data...")
    string = ""
    for i in response.json():
        string = string + f"@{i['user']['username']} {i['id']}\n"

    with open("Relationship_Data.txt", 'w') as f:
        f.write("made by 8c https://github.com/fuck8c\n\n") 
        f.write(string)
    print(Fore.MAGENTA + "relationship data written to Relationship_Data.txt.")
    input('Press enter to exit')
else:
    print(f"failed to fetch relationship data error: {response.status_code}")


# format json
# [{'id': '478514195059703808', 'type': 1, 'nickname': None, 'user': {'id': '478514195059703808', 'username': 'billersun', 'global_name': 'Billy', 'avatar': 'f772c8c3825afcea9325f39ff27d4a8a', 'avatar_decoration_data': None, 'discriminator': '0', 'public_flags': 0}, 'since': '2024-01-03T04:00:09.442000+00:00'}
