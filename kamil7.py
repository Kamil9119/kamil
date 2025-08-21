#>>>>>>> SCRIPT >>>> GIVE BY : MR UNKNOWN 💚
#>>>>>>> TELIGERM : https://t.me/+b7u5TjLAntphZDQ1
import os
import time
import requests
import random

# Install user_agent if not available
try:
    from user_agent import generate_user_agent
except ModuleNotFoundError:
    os.system('pip install user_agent')
    os.system('clear')
    from user_agent import generate_user_agent

user_agent = generate_user_agent()

# Color codes
g = '\x1b[1;32m'  # Green
r = '\x1b[1;31m'  # Red
b = '\x1b[1;34m'  # Blue
c = '\x1b[1;36m'  # Cyan
w = '\x1b[1;37m'  # White

# Wait function
def wait():
    for i in range(100):
        print(f'\n\n{g}[ + ] Please wait for next submission: {i + 1}/120', end='\r')
        time.sleep(1)
        os.system('clear')

# TikTok video booster class
class TikDemoView:
    def __init__(self):
        print(f"{g}Initializing... Please wait a moment!{w}")

    def boost_video(self, user: str, link: str) -> dict:
        response = requests.post(
            'https://api.likesjet.com/freeboost/3',
            json={
                'link': link,
                'tiktok_username': user,
                'email': f'DEMOABOHSN{random.randint(10000, 99999)}@gmail.com'
            },
            headers={
                'Host': 'api.likesjet.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent
            }
        ).json()
        return response

# Main function
def main():
    os.system('clear')
    os.system("xdg-open https://t.me/+b7u5TjLAntphZDQ1")
    os.system("xdg-open https://t.me/+b7u5TjLAntphZDQ1")
    # Logo / Header
    print(f"""{g}
   /$$   /$$ /$$   /$$ /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$  /$$/| $$  | $$| $$  | $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$ /$$/ | $$  | $$| $$  | $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$/  | $$  | $$| $$  | $$| $$  | $$| $$ $$/$$ $$| $$  | $$| $$ $$ $$
| $$  $$  | $$  | $$| $$  | $$| $$  | $$| $$  $$$| $$| $$  | $$| $$  $$$$
| $$\  $$ | $$  | $$| $$  | $$| $$  | $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$ \  $$|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \/  | $$|  $$$$$$/| $$ \  $$
|__/  \__/ \______/  \______/  \______/ |__/     |__/ \______/ |__/  \__/
{w}════════════════════════════════════════════════
{b}[INFO]{w} AUTHOR    : MR UNKNOWN 
{b}[INFO]{w} FACEBOOK  : NOTHING 
{b}[INFO]{w} TELEGRAM  : https://t.me/+b7u5TjLAntphZDQ1
{w}════════════════════════════════════════════════
{b}[INFO]{w} FEATURE   : TIKTOK AUTO VIWS 
{b}[INFO]{w} VERSION   : 0.3
{b}[INFO]{w} STATUS    : {g}FREE{w}
{w}════════════════════════════════════════════════
""")
    user = input(f'{c}Enter TikTok username:{w} ')
    link = input(f'{b}Enter video link:{w} ')

    booster = TikDemoView()
    response = booster.boost_video(user, link)

    if response.get('status'):
        print(f'{g}[√] Successfully sent 1000 views! Enjoy!{w}')
        wait()
        main()
    else:
        print(f"{r}[#] Sorry! Could not send views to your video.{w}")
        wait()
        main()

# Run the script
if __name__ == "__main__":
    main()