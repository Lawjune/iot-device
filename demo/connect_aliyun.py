import sys
import os
# sys.path.append((os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import ssl
import time
from mqtt.mqtt_client import MqttClient

host = "iot-06z00ixr2mvpm49.mqtt.iothub.aliyuncs.com"
port = 1883
keepalive = 60
client_id = "hdusQi48NSt.lawjune_device_001|securemode=2,signmethod=hmacsha256,timestamp=1655305545587|"
username = "lawjune_device_001&hdusQi48NSt"
password = "a763f86833a45b3a14130791f29b703d922ad785d4bebd4a237d9c8e4ca10e25"
device_name = "lawjune_device_001"

def main():
    client_a = MqttClient(host=host, port=port, keepalive=keepalive, client_id=client_id)
    client_a.client.username_pw_set(username=username, password=password)

    client_a.add_topic(f"/hdusQi48NSt/{device_name}/user/get")
    
    client_a.start()
    
    time.sleep(4)
    
    client_a.publish(topic=f"/hdusQi48NSt/{device_name}/user/update", payload="Hello Aliyun")
    
    # client_a.publish(topic="/hdusQi48NSt/{device_name}/user/update", payload="Hello Aliyun")
    while True:
        try:
            msg = input()
        except KeyboardInterrupt:
            client_a.stop()
        if msg == "q":
            client_a.stop()
    

if __name__ == "__main__":
    main()

