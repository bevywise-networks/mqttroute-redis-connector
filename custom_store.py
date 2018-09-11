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

# Change the below values if you are running the Redis in a remote host.

redishost='localhost'
redisport=6379


import redis

import time

global r
r = redis.StrictRedis(host=redishost, port=redisport, db=0)

def handle_Received_Payload(data):

        print data
        client = data['sender']
        unixtime=data['unixtime']
        key = str(client)+'_'+str(unixtime)
        print key

        global r
        r.set(key, data)
