import json


class getPrivate:

    def __init__(self):
        print("init")

        with open("private.json", "r") as data:
            global privateData
            privateData = json.load(data)
            print("JSON Parsed")

    def getToken(self):
        token = privateData["Token"]  # json에서 token을 불러옴(token은 보안을 위해 로컬에 저장되어야 함)
        return token
