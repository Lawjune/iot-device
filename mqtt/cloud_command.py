import json

class CloudCommandException(Exception):
    pass

class CloudCommand:
    topic_suffix = r"command/"
    def __init__(self, command_json=None):
        self.__device_id = None
        self.__service_id = None
        self.__command_name = None
        self.__paras = None
        self.__request_id = None
        if command_json:
            self.__command = json.loads(command_json)
        else:
            self.__command = dict()
        self.__set_command()

    def jsonify(self):
        return json.dumps(self.__command)

    def __set_command(self):
        if 'device_id' in self.__command.keys():
            self.__device_id = self.__command['device_id']
        if 'command_name' in self.__command.keys():
            self.__command_name = self.__command['command_name']
        if 'service_id' in self.__command.keys():
            self.__service_id = self.__command['service_id']
        if 'paras' in self.__command.keys():
            self.__paras = self.__command['paras']
        if 'request_id' in self.__command.keys():
            self.__request_id = self.__command['request_id']

    @property
    def service_id(self):
        return self.__service_id
    
    @service_id.setter
    def service_id(self, value):
        self.__command['service_id'] = value
        self.__service_id = value
        return self

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        self.__command['device_id'] = value
        self.__device_id = value    
        return self

    @property
    def command_name(self):
        return self.__command_name

    @command_name.setter
    def command_name(self, value):
        self.__command['command_name'] = value
        self.__command_name = value
        return self

    @property
    def paras(self):
        return self.__paras

    @paras.setter
    def paras(self, value):
        self.__command['paras'] = value
        self.__paras = value
        return self

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__command['request_id'] = value
        self.__request_id = value
        return self


