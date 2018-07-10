
import requests
from requests.auth import HTTPBasicAuth
import json

DomainApiRecordsUrl = 'https://api.name.com/v4/domains/bestchoice.live/records'
PublicIpUrl = 'http://ip.42.pl/raw'
DomainApiUrl = 'https://api.name.com/v4/domains/your-choice.today/url/forwarding'
User = 'mazen.imara'
Token = '8489e7bd64aeeacc86739d4964ab0676a540ec2d' 


def checkIp():
	publicIp = None
	oldIp = None
	status = False
	try:
		publicIp = requests.get(PublicIpUrl).text
	except requests.exceptions.RequestException as e:
		print(e)

	if publicIp:
		try:
			records = getRecords()
			oldIp = records[0]['answer']
		except Exception as e:
			print(e)
	
	 		
	#publicIp = '192.168.1.1'
	if publicIp and oldIp and publicIp != oldIp:
		status = True
	result = {
		'status': status,
		'newIp': publicIp,
		'records': records

	}
	return result

def getRecords():
	records = None
	try:
		auth=HTTPBasicAuth(User, Token)
		r = requests.get(DomainApiRecordsUrl, auth=auth)
	except requests.exceptions.RequestException as e:
		print(e)

	try:
		records = r.json()['records']		
	except Exception as e:
		print(e)

	if records != None and len(records) == 0:
		records = None
	return records



def updateRecordIp(record, newIp):
	res = None
	data = {
		'answer': newIp,
	}
	data = json.dumps(data)
	try:
		auth=HTTPBasicAuth(User, Token)
		r = requests.put(DomainApiRecordsUrl + '/' + str(record['id']), data=data, auth=auth)
		res = r.text
	except requests.exceptions.RequestException as e:
		print(e)
	print(res)


def updateRecordsIp():
	checkip = checkIp()
	print(checkip)
	if checkip and checkip['status']:
		for record in checkip['records']:
			updateRecordIp(record, checkip['newIp'])

