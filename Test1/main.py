from datetime import datetime
from datetime import timezone 
import datetime 
import time
import paho.mqtt.client as mqtt
import json
import base64
import cv2

#-------------------------------------------------------------
#COSAS DE MQTT
#-------------------------------------------------------------
client = mqtt.Client("pruebasDistribuidos")
client.connect("", port=)

def get_image_array():
    images = []
    for i in range(0, 61):
        with open("images/image ({}).jpg".format(i),'rb') as file:
            filecontent = file.read()
            encoded = base64.b64encode(filecontent)
            base = str(encoded)
            images.append(base)
    return images


def time_to_str(): return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


def sendData_ditto_protocol(group, rep, msg, time):
    message = {
        "topic" : "distributed/imagerecognition/things/twin/commands/merge",
        "headers":{
            "content-type": "application/merge-patch+json"
        },
        "path": "/features",
        "value": {
            "group": {
                "properties": {
                    "value": group
                }
            },
            "rep": {
                "properties": {
                    "value": rep
                }
            },
            "msg": {
                "properties": {
                    "value": rep
                }
            },
            "image": {
                "properties": {
                    "value": msg
                }
            },
            "timestamp": {
                "properties": {
                    "value": time
                }
            }
        }
    }
    message = json.dumps(message)
    client.publish("telemetry/distributed", payload = message)


def main():
    images = get_image_array()
    for group in range(0, 11):
        print("Bloque {}".format(group))
        for rep in range(0, 10):
            print("Repeticion {}".format(rep))
            
            for message in range(0, (group+1)*10):
                dt = datetime.datetime.now(timezone.utc)  
                utc_time = dt.replace(tzinfo=timezone.utc) 
                utc_timestamp = utc_time.timestamp()
                sendData_ditto_protocol(group, rep, message, images[0], utc_timestamp)
            time.sleep(10)
        time.sleep(15)

if __name__ == "__main__":
    main()