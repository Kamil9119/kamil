import os, requests
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt

#https://t.me/+9llqPQbiQ1hiN2Vl/

"""
TELEGRAM: https://t.me/+9llqPQbiQ1hiN2Vl
"""

def fetch():
    try:
        u1 = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=0").text
        u2 = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=0").text
        u3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/http.txt").text
        u4 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/refs/heads/master/https.txt").text
        with open("/sdcard/proxies.txt", "w") as f:
            f.write(u1 + "\n" + u2 + "\n" + u3 + "\n" + u4)
    except:
        pass

try:
    proxies = open("/sdcard/AML_PROJECT/proxies.txt").read().splitlines()
except:
    proxies = []

def clear():
    os.system('clear')
def line():
    print(40*"-")

def get_proxy():
    for p in proxies:
        if p.strip():
            return p.strip()

def get_link():
    clear()
    print(Panel.fit("TELEGRAM AUTO VIEW",border_style="bold green", title="[bold white] UNKNOWN"))
    link = Prompt.ask(f"[bold green]╭──([bold green]💀ENTER LINK🔗💀[bold green]) \n╰──▶")
    limit = Prompt.ask(f"[bold green]╭──([bold green]💀ENTER LIMIT💀[bold green]) \n╰──▶")
    return link,limit

#Make sure give credit O⁠_⁠o
def main():
    post,limit = get_link()
    clear()
    channel, msg_id = post.split('/')[3], post.split('/')[4]
    print(Panel.fit("TELEGRAM AUTO VIEW",border_style="bold green", title="[bold white] UNKNOWN"))
    print(Panel.fit(f"LINK : {channel} LIMIT : {limit}",border_style="bold green"))
    for i in range(int(limit)):
        proxy = get_proxy()
        try:
            s = requests.Session()
            p = {'http': proxy, 'https': proxy}
            r = s.get(f"https://t.me/{channel}/{msg_id}",proxies=proxy)
            c = r.headers.get('set-cookie', '').split(';')[0]
            h = {"Cookie": c, "User-Agent": "Chrome", "Referer": f"https://t.me/{channel}/{msg_id}?embed=1"}
            r2 = s.post(f"https://t.me/{channel}/{msg_id}?embed=1", json={"_rl": "1"}, headers=h, proxies=p)
            k = r2.text.split('data-view="')[1].split('"')[0]
            v = r2.text.split('class="tgme_widget_message_views">')[1].split('<')[0].replace("K", "00").replace(".", "")
            h2 = {"Cookie": c, "X-Requested-With": "XMLHttpRequest", "User-Agent": "Chrome"}
            r3 = s.get(f"https://t.me/v/?views={k}", headers=h2, proxies=p)
            if "true" in r3.text:
                print(f'[bold green]VIEW ADDED 👉 {v}')
            else:
                print(f"[bold red]FAILED TO SEND 👉 {v}")
        except:
            pass
        
if __name__ == "__main__":
    fetch()
    main()
