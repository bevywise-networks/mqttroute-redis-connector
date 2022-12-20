#################################################################
# @Bevywise.com IOT Initiative. 
# www.bevywise.com Email - support@bevywise.com
#
# custom_store.py
#
# This plugin helps in pushing the payload received from 
# the edge clients to a redis server for further processing. 
#
# The parameter data will be in dict format and the keys are 
# 'sender','topic', 'message', 'unixtime', 'timestamp'
# This plugin createes a key using the clientid and the 
# unixtime which will create an unique combination. The values 
# are added to redis as received in the same dict format. 
#
# IMPORTANT - The key will fail if a client send more than 
# one message per second 
#
#################################################################

import redis
import json


# Change the below values if you are running the Redis in a remote host.
redishost = 'localhost'
redisport = 6379

global redis_conn
redis_conn = redis.StrictRedis(host=redishost, port=redisport, db=0)

def handle_Received_Payload(data):
	try:
		global redis_conn
		client = data['sender']
		unixtime = data['unixtime']
		key = str(client)+'_'+str(unixtime)
		print('Key:', key, ' Data:', data)
		if isinstance(data, dict):
			data = json.dumps(data)
		redis_conn.set(key, data)
	except Exception as e:
		print(e)
