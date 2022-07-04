import logging

from mqtt.mqtt_client import MqttClient
from mqtt.cloud_command import CloudCommand, CloudCommandException
from mqtt.device_message import DeviceMessage
from static import remote_commands

class MqttCommand(MqttClient):
    topic_prefix = r"remoteControl/vehicle/"
    def __init__(self, host, port, keepalive, device_id, logging_level=logging.DEBUG):
        self.__device_id = device_id
        super(MqttCommand, self).__init__(host=host, port=port, 
                                          keepalive=keepalive, client_id=device_id + r"_client", 
                                          logging_level=logging_level)

        self.__pub_topic = f"{self.topic_prefix}{self.__device_id}/{CloudCommand.topic_suffix}"
        self.__sub_topic = f"{self.topic_prefix}{self.__device_id}/{DeviceMessage.topic_suffix}"

        self.add_topic(self.__sub_topic)
        self.set_on_message_callback(self.__on_message)

    def send_command(self, command):
        if isinstance(command, CloudCommand):  
            command.device_id = self.client_id
            self.publish(topic=self.__pub_topic, payload=command.jsonify())     
        else:
            raise CloudCommandException("Invalid input command.")

    def __on_message(self, client, userdata, msg):
        self.__on_device_message(msg.payload)

    def __on_device_message(self, raw_message):
        message = DeviceMessage(raw_message)
        self.logger.debug(f"Recieved device message: {message.jsonify()}")
        

if __name__ == "__main__":
    import time

    host = "localhost"
    port = 1883
    keepalive = 60

    mqtt_cmd = MqttCommand(host=host, port=port, keepalive=keepalive, 
                           device_id="virtualDevice007")
    mqtt_cmd.set_username_and_password(username="remoteControlCommand", password="Pass1234")

    door_lock_cmd = CloudCommand()
    door_lock_cmd.command_name = remote_commands.COMMAND_REMOTE_DOORUNLOCK

    door_unlock_cmd = CloudCommand()
    door_unlock_cmd.command_name = remote_commands.COMMAND_REMOTE_DOORUNLOCK

    mqtt_cmd.start()
    time.sleep(4)
    mqtt_cmd.send_command(door_lock_cmd)
    time.sleep(4)
    mqtt_cmd.send_command(door_unlock_cmd)
    time.sleep(300)