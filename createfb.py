import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
logo4 = """\033[1;97m
 ___      ___  ___  ___   ________  
|"  \    /"  ||"  \/"  | /"       ) 
 \   \  //   | \   \  / (:   \___/  
 /\\  \/.    |  \\  \/   \___  \    
|: \.        |  /\.  \    __/  \\   
|.  \    /:  | /  \   \  /" \   :)  
|___|\__/|___||___/\___|(_______/ 
--------------------------------------------------
\033[1;97m AUTHOR :\033[1;92m MALIK SOHAIL \033[1;97m:/
\033[1;97m GitHub :\033[1;92m MR-JANI-906 \033[1;97m:/
\033[1;97m Version:\033[1;92m 7.0 \033[1;97m:/
\033[1;97m Status :\033[1;92m PREMIUM \033[1;97m:/
\033[1;97m Notice : Use Sim Deta 100094/10008 For More OK Ids:/
--------------------------------------------------
 \33[37;41m\t DEAR USERS NEED A GIRLFRIEND:👀💔 \33[0;m
\033[1;37m[!]  WIFI WORKING BUT USE NEW FILE WORK:
--------------------------------------------------"""
boy = ['Ali Khan', 'Rustam Khan', 'Faisal Khan', 'Afzal Khan', 'Haider Khan', 'Suleman Khan', 'Nadeem Khan', 'Nazeer Malik', 'Nazeer Jutt', 'Nazeer Rehmani', 'Safdar Malik', 'Intzar Khan', 'Saleem Malik', 'Abdullah Malik', 'Naseer Jutt', 'Muzammil Malik', 'Fiaz Ahmad', 'Asghar Ali', 'Shabeer Ahmad', 'Irfan Ali', 'Ahmad Gujjar']
girl = ['Sajida Malik', 'Ayesha Khan', 'Nabeela Malik', 'Kinza Fatima', 'Arooj Khan', 'Muskan Khan', 'Ayesha Malik', 'Safina Malik', 'Nida Ali', 'Rimsha Ali']
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('            Auto create tool')
    print (47*'-')
    print ('[1]auto creat')
    print ('[2]join Facebok group')
    print ('[3] join whatsapp group')
    print (47*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://www.facebook.com/groups/262660289344669/?ref=share_group_link')
        menu()
    elif sel in ['3', '03']:
        os.system('xdg-open https://chat.whatsapp.com/C4EokyLxEaZGBlyJ99M3pA')
        menu()
    if sel in['4', '04']:
    	tfa().start()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
        
class tfa:
        def __init__(self):
        	self.loop = 0
            self.gender = []
         def start(self):
         	    os.system('clear')
    print (logo4)
    print ('\033[0;97mExample email==password==cookie')
    print ('\033[0;97mFIRST PAST UID ID LINK == YEH LGA KY NEXT PASSWORD ADD KRO')
    user=input('paste: ')
    if user == '':
        menu()
    try:
        email=user.split('==')[0]
        pw=user.split('==')[1]
        cok=user.split('==')[2]
    except:
        print ('put right method of email password cookie')
        time.sleep(3)
        tfa()
    email = email
    pw = pw
    coki=cok.replace(' ', '')
    cokie = coki+';'
    try:
        datr=cokie.split('datr=')[1].split(';')[0]
        fr=cokie.split('fr=')[1].split(';')[0]
        c_user=cokie.split('c_user=')[1].split(';')[0]
        xs=cokie.split('xs=')[1].split(';')[0]
        cokiee='datr='+datr+';'+'fr='+fr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    except:
        try:
            datr=cokie.split('datr=')[1].split(';')[0]
            c_user=cokie.split('c_user=')[1].split(';')[0]
            xs=cokie.split('xs=')[1].split(';')[0]
            cokiee='datr='+datr+';'+'c_user='+c_user+';'+'xs='+xs+';'
        except:
            print ('Cookie not accept')
            exit()
    cookie=cokiee
    language(cookie)
    try:
        try:
            a=ses.get('https://x.facebook.com/security/2fac/setup/intro/metadata/?source=1&paipv=0', cookies={'cookie': cookie})
            bc=BeautifulSoup(a.text, 'html.parser')
            checkcp(bc)
            if '/login.php?next=' in str(bc):
                print ('Maybe your account cp or lock login your account in your kiwi browser if get login success then take new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            elif 'facebook.com/zero/toggle/nux/' in str(bc):
                print ('Cokie not accept first login account in your kiwi browser and get new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            else:
                pass
        except requests.exceptions.SSLError:
            os.system('clear')
            print (logo4)
            print ('internet problem')
            time.sleep(3)
            menu()
        except requests.exceptions.ConnectionError:
            os.system('clear')
            print (logo4)
            print ('internet problem')
            time.sleep(3)
            menu()
        for y in bc.find_all("a",href=True):
            if '/zero/optin/write/?action=cancel' in str(y):
                ref=y.get('href')
                try:
                    aj=BeautifulSoup(ses.get('https://x.facebook.com'+ref, cookies={'cookie': cookie}).text, 'html.parser')
                    checkcp(aj)
                except requests.exceptions.SSLError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                except requests.exceptions.ConnectionError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                for x in aj.find_all('form', {'method': 'post'}):
                    if '/zero/optin/write/?action=confirm' in str(x):
                        link=x.get('action')
                        use=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                        for t in use:
                            use1=t
                        dog={}
                        for z in x('input'):
                            dog.update({z.get("name"):z.get("value")})
                        dog.update({'submit': use1})
                        aa=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dog, cookies={'cookie': cookie}).text, 'html.parser')
                        a=ses.get('https://x.facebook.com/security/2fac/setup/intro/metadata/?source=1&paipv=0', cookies={'cookie': cookie})
                        bc=BeautifulSoup(a.text, 'html.parser')
                        checkcp(bc)
    except requests.exceptions.SSLError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        tfa()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        tfa()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()
    except Exception as e:
        pass
    try:
        for x in bc.find_all("a",href=True):
            if '/security/2fac/setup/qrcode/generate' in str(x):
                link=x.get('href')
                try:
                    b=ses.get(link.replace('m.facebook', 'x.facebook'), cookies={'cookie': cookie})
                    bb=BeautifulSoup(b.text, 'html.parser')
                    checkcp(bb)
                except requests.exceptions.SSLError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                except requests.exceptions.ConnectionError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                for x in bb.find_all('form', {'method': 'post'}):
                    if '/password/reauth/?next=' in str(x):
                        link1=x.get('action')
                        bl=['fb_dtsg', 'jazoest']
                        data={}
                        for v in x('input'):
                            if v.get("name") in bl:
                                try:
                                    data.update({v.get("name"):v.get("value")})
                                except:
                                    pass
                        data.update({'pass': pw, 'save': re.search('type="password" /></div><input value="(.*?)"', str(b.text)).group(1)})
                        try:
                            c=BeautifulSoup(ses.post(link1.replace('m.facebook', 'x.facebook'), data=data, cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(c)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        #secret=re.findall('authentication app</div><div class=".*?">(.*?)</div></div></div></td></tr></table></div></div><div><div', str(c))
                        try:
                            secret=re.findall('data-testid="key">(.*?)</div></div></div></div></div></div></div><div', str(c))
                        except:
                            print ('Password wrong')
                            exit()
                        for y in secret:
                            z=y
                        open('/sdcard/2fakey.txt', 'a').write(email+'|'+pw+'|'+z+'\n')
                        key=z.replace(' ', '')
                        a=requests.get('https://2fa.live/tok/'+key)
                        b1=a.text
                        token = re.sub('[^0-9]', '', b1)
                        gl=['fb_dtsg', 'jazoest']
                        data1={}
                        for x in c('input'):
                            if x.get("name") in gl:
                                try:
                                    data1.update({x.get("name"):x.get("value")})
                                except:
                                    pass
                        data1.update({'code': token})
                        code=BeautifulSoup(ses.post('https://x.facebook.com/security/2fac/setup/verify_code/?paipv=0', data=data1, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(code)
                        try:
                            ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(ad)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(1)
                            menu()
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for g in x('input'):
                                    if g.get("name") in hl:
                                        try:
                                            dat.update({g.get("name"):g.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                print ('Key > '+z)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('Press enter to back')
                                menu()
                for d in bb.find_all("a",href=True):
                    if 'otpauth://totp/ID:'+email in d.get('href'):
                        secret=re.findall('data-testid="key">(.*?)</div></div></div></div></div></div></div><div', str(bb))
                        for y in secret:
                            z=y
                        open('/sdcard/2fakey.txt', 'a').write(email+'|'+pw+'|'+z+'\n')
                        key=z.replace(' ', '')
                        a=requests.get('https://2fa.live/tok/'+key)
                        b1=a.text
                        token = re.sub('[^0-9]', '', b1)
                        gl=['fb_dtsg', 'jazoest']
                        data1={}
                        for m in bb('input'):
                            if m.get("name") in gl:
                                try:
                                    data1.update({m.get("name"):m.get("value")})
                                except:
                                    pass
                        data1.update({'code': token})
                        code=BeautifulSoup(ses.post('https://x.facebook.com/security/2fac/setup/verify_code/?paipv=0', data=data1, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(code)
                        try:
                            ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(ad)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                print ('Key > '+z)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
            elif '/security/2fac/factors/recovery-code/' in str(x) or '/security/2fac/setup/turn_off' in str(x):
                print ('2fa alreaf on this account')
                print ('You want recovery codes? y/n')
                yes=input('Select: ')
                if yes=='y':
                    try:
                        ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(ad)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        try:
                            os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                        except:
                            pass
                        try:
                            red=open('.key.txt', 'r').read()
                            zed=red.split('|')[2].split('\n')[0]
                        except:
                            zed='Key not found'
                        print ('Key > '+zed)
                        coded(ad)
                        print ('successfuly 2fa done')
                        input('press enter to back')
                        menu()
                    except:
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('name="resend" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                try:
                                    os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                                except:
                                    pass
                                try:
                                    red=open('.key.txt', 'r').read()
                                    zed=red.split('|')[2].split('\n')[0]
                                except:
                                    zed='Key not found'
                                print ('Key > '+zed)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
                else:
                    menu()
        for x in bc.find_all('form', {'method': 'post'}):
            if '/password/reauth/?next=' in str(x):
                das={}
                link=x.get('action')
                print ('2fa already on this account')
                print ('You want recovery codes y/n')
                yes=input('Select: ')
                if yes=='y':
                    bl=['fb_dtsg', 'jazoest']
                    for y in x('input'):
                        if y.get("name") in bl:
                            try:
                                das.update({y.get("name"):y.get("value")})
                            except:
                                pass
                    das.update({'pass': pw, 'submit': re.search('type="password" /></div><input value="(.*?)"', str(a.text)).group(1)})
                    try:
                        c=BeautifulSoup(ses.post(link.replace('m.facebook', 'x.facebook'), data=das, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(c)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(ad)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        try:
                            os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                        except:
                            pass
                        try:
                            red=open('.key.txt', 'r').read()
                            zed=red.split('|')[2].split('\n')[0]
                        except:
                            zed='Key not found'
                        print ('Key > '+zed)
                        coded(ad)
                        print ('successfuly 2fa done')
                        input('press enter to back')
                        menu()
                    except:
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('name="resend" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                try:
                                    os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                                except:
                                    pass
                                try:
                                    red=open('.key.txt', 'r').read()
                                    zed=red.split('|')[2].split('\n')[0]
                                except:
                                    zed='Key not found'
                                print ('Key > '+zed)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
                else:
                    menu()
        print ('data not found')
        input('Press enter to back')
        menu()
    except requests.exceptions.SSLError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()
    except Exception as e:
        print ('data not found')
        input('Press enter to back')
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] Boys name ids')
        print ('[2] girls name ids')
        print (47*'-')
        gen = input('select: ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example 1000, 2000, 5000, 10000')
        lim = int(input('limit: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
        }
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[Creat-fb] {OO}{self.loop}/{str(lim)} OK:{len(ok)} - CP:{len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m[OK] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (47*'-')
        print ('\033[1;32mTotal ids > Ok/' +str(len(ok)) + ' CP/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()
