import os
from extractor import Extractor


class Main:
    ex = Extractor()
    url = ""
    def __init__(self) -> None:
        os.system("cls")
        print("\n\n")
        print("----------- Welcome to Keyword Extractor for Fiverr ------")
        print("\n\n")
        url = input("Enter gig url : ")
        self.ex.getHtmlContents(url)

Main()
