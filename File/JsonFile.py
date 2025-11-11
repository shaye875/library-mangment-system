from File.File import File
import json


class JsonFile(File):

    @staticmethod
    def read(file_name):
        with open(file_name, 'r') as f:
            json_data = json.loads(f.read())
            return json_data

    @staticmethod
    def write(file_name, arr):
        json_arr = JsonFile.convert_to_json(arr)

        with open(file_name, 'w') as f:
            f.write(json.dumps(json_arr))

    @staticmethod
    def convert_to_json(arr):
        return [obj.to_dictionary() for obj in arr]







