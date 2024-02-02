import json

class database:

    user_list = []
    
    def __init__(self) -> None:
        self.f = open("database.json")
        self.data = json.loads(self.f.read())
        self.user_list = self.data["accounts"]

    def saveLogin(self, email, password):
        data = {'email':email, 'password':password}
        app_json = json.dumps(data)
        f = open('loggedIn.json', mode='w')    
        f.write(app_json)
        f.close()


    def register(self, email, password):

        if self.checkPassword(email=email, password=password):
            print("Already has account.")
            return False
        
        data = {'email':email, 'password':password}
        self.user_list.append(data)
        d = {"accounts" : self.user_list}
        app_json = json.dumps(d)
        f = open('database.json', mode='w')    
        try:
         f.write(app_json)
         f.close()
         return True
        except Exception as e:
            return False


    def checkPassword(self, email, password):
        for i in self.user_list:
            if i["email"] == email:
                if i["password"] == password:
                    self.saveLogin(email, password)
                    return True 
        # print("No user found.")     
        return False   
                