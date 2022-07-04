import json
class DeviceMessage:
    topic_suffix = r"message/"
    return_status_success = 0
    return_status_error = 1
    return_status_failed = 2
    
    def __init__(self, message_json=None):
        if message_json is None:
            self.__message = dict()
        else:
            self.__message = json.loads(message_json)
        self.__device_id = None
        self.__message_id = None
        self.__name = None
        self.__content = None
        self.__set_message()

    def __set_message(self):
        if 'device_id' in self.__message.keys():
            self.__device_id = self.__message['device_id']
        if 'id' in self.__message.keys():
            self.__message_id = self.__message['id']
        if 'name' in self.__message.keys():
            self.__name = self.__message['name']
        if 'content' in self.__message.keys():
            self.__content = self.__message['content']

    def jsonify(self):
        return json.dumps(self.__message)

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__message['device_id'] = value
        self.__device_id = value

    @property
    def message_id(self):
        return self.__message_id

    @message_id.setter
    def id(self, value):
        self.__message['message_id'] = value
        self.__message_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__message['name'] = value
        self.__name = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__message['content'] = value
        self.__content = value


