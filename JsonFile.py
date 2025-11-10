from File import File
import json


class JsonFile(File):

    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name, 'r') as f:
            json_data = json.loads(f.read())
            return json_data

    def write(self, arr):
        json_arr = self.convert_to_json(arr)

        with open(self.file_name, 'w') as f:
            f.write(json.dumps(json_arr))

    def convert_to_json(self, arr):
        return [obj.__dict__() for obj in arr]







