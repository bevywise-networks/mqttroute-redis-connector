## mqttroute-redis-connector

This plugin connects MQTTRoute with the Redis server to store all the payload to the redis server for the further processing.  

# MQTTRoute 
MQTTRoute is a powerful and high performance MQTTBroker that enables communication between various MQTT Devices and MQTT Sensors. MQTTRoute has FREE and affordable premium versions. 

# configure and setup 
	1. Replace custom_store.py with Bevywise/MQTTRoute/lib/custom_store.py.
	2. In custom_store.py Change the server name and the port of the Redis if you are running Redis on a different server or port
	2. Open Bevywise/MQTTRoute/conf/data_store.conf 
		1. Update CUSTOMSTORAGE = ENABLED
		2. Update DATASTORE = CUSTOM 
	3. Start the MQTTRoute and it will start storing all the payload into Redis Server with clientId_unixtime as the key. 
