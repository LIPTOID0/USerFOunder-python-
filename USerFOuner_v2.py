import requests
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_user(username):
    if username.lower() in ['liptoid', 'liptoid', 'LIPTOID']:
        print("\033[91m  Don't mess with the developer!")
        return

    sites = [
        "https://discord.com/users/{}".format(username),
        "https://github.com/{}".format(username),
        "https://www.youtube.com/user/{}".format(username),
        "https://www.snapchat.com/add/{}".format(username),
        "https://www.pinterest.com/{}/".format(username),
        "https://www.reddit.com/user/{}".format(username),
        "https://support.mozilla.org/en-US/user/{}".format(username),
        "https://freebitco.in/{}".format(username),
        "https://www.instagram.com/{}/".format(username),
        "https://twitter.com/{}".format(username),
        "https://www.tiktok.com/@{}".format(username),
        "https://www.facebook.com/{}".format(username),
        "https://www.ludo.com/profile/{}".format(username),
        "https://www.blogger.com/profile/{}".format(username),
        "https://plus.google.com/{}/".format(username),
        "https://wordpress.com/{}".format(username),
        "https://open.spotify.com/user/{}".format(username),
        "https://www.roblox.com/user.aspx?username={}".format(username),
        "https://www.wattpad.com/user/{}".format(username),
        "https://www.amazon.com/hz/wishlist/ls/{}".format(username),
        "https://www.aliexpress.com/store/{}".format(username),
        "https://www.linkedin.com/in/{}".format(username),
        "https://www.youtube.com/channel/{}".format(username),
        "https://www.happymod.com/profile/{}".format(username),
        "https://www.messenger.com/t/{}".format(username),
        "https://www.torproject.org/about/contact.html.en"
    ]

    found = False

    for site in sites:
        response = requests.get(site)
        if response.status_code == 200:
            print("\033[92mFound :)", site)
            found = True
        else:
            print("\033[91mNot Found :(", site)

    if not found:
        print("\033[91mUser not found on any site.")

clear_screen()
print("""
 _   _                  __                      _           
| | | |                / _|                    | |          
| | | |___  ___ _ __  | |_ ___  _   _ _ __   __| | ___ _ __ 
| | | / __|/ _ \ '__| |  _/ _ \| | | | '_ \ / _` |/ _ \ '__|
| |_| \__ \  __/ |    | || (_) | |_| | | | | (_| |  __/ |   
 \___/|___/\___|_|    |_| \___/ \__,_|_| |_|\__,_|\___|_|   
                                                            
GitHub: https://github.com/LIPTOID0
Bitcoin Wallet for Donations: bc1qzmd58zt8za7uzjtgngmg99a69gg04f4knk7mm7
""")

while True:
    username = input("Please enter the username to check (or 'exit' to quit): ")
    if username.lower() == 'exit':
        break
    check_user(username)
    input("Press any key to continue...")
    clear_screen()
