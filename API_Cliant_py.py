import requests

class API_Cliant():
    def __init__(self, refresh='', access=''):
        self.refresh = refresh
        self.access = access
        
    def login(self):
        login_url = 'https://register-manager.herokuapp.com/api/user/login'
        credentials = {"email": "rabby12@gmail.com", "password": "11223344"}
        try:
            user_login = requests.post(url=login_url, data=credentials).json()
            
            if 'errors' in user_login:
                errors = user_login['errors']
                print(errors)
            elif not 'errors' in user_login:
                self.refresh = user_login['token']['refresh']
                self.access = user_login['token']['access']
                return user_login
        except Exception as e:
            print('Somethin wrong')
    
    def profile(self):
        self.login()
        profile_url = 'https://register-manager.herokuapp.com/api/user/profile'
        headers = {'accept': 'application/json', 'authorization': "Bearer "+ self.access}
        
        user_profile = requests.get(url=profile_url, headers=headers).json()
        print('profile : '+str(user_profile))
        
        




api = API_Cliant()
# api.login()
api.profile()