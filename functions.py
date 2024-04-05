import json

class get:
    class getData:
        def __init__(self):
            self.data = ""
        def Token(self):
            with open("private.json", "r") as JSONData:
                self.data = json.load(JSONData)
                print("JSON Parsed")
                return(self.data["Token"])