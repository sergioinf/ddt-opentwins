# python3.6

import random
from datetime import datetime
from datetime import timezone 
import datetime 
from paho.mqtt import client as mqtt_client
import json

broker = ''
port = 
topic = "opentwins/live/messages/prueba/#"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'

todos = []

def time_to_str(): return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        new_json = json.loads(msg.payload.decode("utf-8"))
        new_json = new_json['value']
        
        
        
        dt = datetime.datetime.now(timezone.utc)  
        utc_time = dt.replace(tzinfo=timezone.utc) 
        utc_timestamp = utc_time.timestamp()
        new_json['sendingBackTime_Final'] = utc_timestamp
        
        print("Nuevo")
        todos.append(new_json)
        
        if len(todos) == 5510:
            with open('results.json', 'w') as outfile:
                json.dump(todos, outfile)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
