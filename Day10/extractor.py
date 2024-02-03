import requests
import re
import json

class Extractor:
    url = ""

    def __init__(self) -> None:
       pass

    def getHtmlContents(self, url):
            s = requests.Session()
            payload = {}
            headers = {
                 "User-agent":"PostmanRuntime/7.36.1",
                 "Accept":"*/*",
                 "Accept-Encoding":"gzip, deflate, br"
            }
            response = s.request("GET", url, headers=headers, data=payload)
            pattern = re.compile(r'<script type="application/json" id="perseus-initial-props">(.*?)</script>', re.DOTALL)
            match = pattern.search(response.text)
            if match:
                script_content = match.group(1)
                data = json.loads(script_content)
                # print(data["description"]["content"])
                print("----------------------------------------")
                print("Content Loaded.")
                print("title - To show Title")
                print("des - To show Description")
                print("tags - To show Tags")
                while True:
                 print("-----------------------------------")
                 command = input("Enter : ")
                 match command:
                     case "title":
                          print(data['general']['gigTitle'])
                     case "des":
                          print(data["description"]["content"])
                     case "tags":
                          ls = data["tags"]["tagsGigList"]
                          for i in ls:
                               print(i["name"])
                     case _:
                         print("Exiting...")
                         break             
    
            else:
                print("Script tag not found.")
