import json

class get:
    def __init__(self):
        self.data = ""
    def Token(self):
        with open("private.json", "r") as JSONData:
            self.data = json.load(JSONData)
            print("JSON Parsed")
            return(self.data["Token"])
                
#내가보기에 이거 어짜피 한번 콜 해줘야되니까
#걍 어....겟 있어야되나?
#다른 러이브러리들 참고해서 고쳐야되긴 함
#뭐가 문젠진 모름