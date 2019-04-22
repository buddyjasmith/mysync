import os
import sys

import json




class User:

    def __init__(self):
        """
        Looks in the default location for user info and stores it in a dictionary
        """
        self.json_path = '../user_info/user.json'
        self.user = self.check_json_exist()
        

    def is_json(self, myjson):
        """
        checks if file is of json type
        """
        try:
            json_object = json.loads(myjson)

        except ValueError as e:
            return False
        return True

    def check_json_exist(self):
        """
        opens json file reads the content of json into dict, returns dict.
        if bad read, empty dict is returned
        """
        try:
            f = open(self.json_path, "r")
            data = f.read()

            if self.is_json(data):
                return json.loads(data)
            else:
                raise IOError
        except IOError:
            print("Error Collecting or reading data.  Check Json contents")
        return {}

    def get_user_info(self):
        return self.user







