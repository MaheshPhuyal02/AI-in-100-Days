import os
import requests
import re

class Translator:
    host = "https://translate.google.com/m?sl={sl}&tl={tl}&q={q}"
    sl = ""
    tl = ""
    query = ""

    def getData(self):
        response = requests.request(method="GET",
                                url= self.host.format(sl = self.sl, tl = self.tl, q = self.query),
                                data={})
        self.extract(response=response)

    def extract(self, response):
        # print(response.text)
        pattern = r'<div class="result-container">(.*?)<\/div>'
        match = re.search(pattern, response.text)

        if match:
            result_value = match.group(1)
            print(str(result_value))
        else:
            print("No match found.")


    def __init__(self) -> None:
        os.system("cls")
        print("\n\nWelcome to Translator \n\n")
        self.sl =input("Enter source language code : ")
        self.tl =input("Enter target language code : ")
        self.query = input("Enter text to convert : ")
        self.getData()

Translator()       

        
        