import json
import requests
import time
import base64
import os

cloud_url = 'https://thingspace.io/dweet/for/'
thing_name = 'hello'

while True:
	overall_data ={}
	millis = int(round(time.time()))
	overall_data['timestamp'] = str(millis)
	overall_data['temperature'] = 30
	overall_data['humidity'] = 60
 	overall_data['vibration'] = 50
	overall_data['proximity'] =  50


       	#json_data = json.dumps(overall_data)
	json_data = json.dumps(overall_data,sort_keys=False)
	print json_data
	url = cloud_url + thing_name
	print url  
	headers = {'content-type': 'application/json'}
	s = {}
	try:
		resp = requests.post(url=url,headers=headers,data=json_data)
		status = resp.status_code
		s = 'status=' + str(status)
		print 'status=' + str(status)
		
	except requests.exceptions.RequestException as e:
		print e
		#print  "Error: {}".format(e)
		time.sleep(50)
		continue
        #resp = requests.post(url=url,headers=headers,data=json_data)
	time.sleep(10)
