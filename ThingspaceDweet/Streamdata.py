import json
import requests
import time
import base64
import os

url = 'https://thingspace.io/listen/for/dweets/from/sensorData'

try:
	session = requests.Session()
	request = requests.Request("GET", url).prepare()
	resp = session.send(request, stream=True)
	
	if resp.encoding is None:
		resp.encoding = 'utf-8'
	'''
	
	'''
	status = resp.status_code
	s = 'status=' + str(status)
	print 'status=' + str(status)
	sensor_data =''
	l = 0 
	for i in resp.iter_lines():
		if i:
			sensor_data = i.decode('ascii')
			l +=1
			#print 'l =' + str(l)
		if l ==2 :
			l=0		
			json_data=sensor_data
			print json_data
			s = json.loads(json.loads(json_data))
			
			print s 
			print s['thing']
			print s['content']['temperature']	
			#break;
			
			
			
except requests.exceptions.RequestException as e:
	print e
	print  "Error: {}".format(e)
	time.sleep(50)


