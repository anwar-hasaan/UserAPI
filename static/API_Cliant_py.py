import requests

class API_Cliant():
    def __init__(self, refresh='', access=''):
        self.refresh = refresh
        self.access = access
        
    def login(self, email, password):
        login_url = 'https://register-manager.herokuapp.com/api/user/login'
        credentials = {"email": email, "password": password}
        try:
            user_login = requests.post(url=login_url, data=credentials).json()
            if 'errors' in user_login:
                errors = user_login['errors']
                print(errors)
            elif not 'errors' in user_login:
                self.refresh = user_login['token']['refresh']
                self.access = user_login['token']['access']
                print(user_login['message'])
            return user_login
        except Exception as e:
            print('Somethin wrong while login')
    
    def register(self, email, name, tc, password, password2):
        register_url = 'https://register-manager.herokuapp.com/api/user/register'
        data = {'email': email, 'name': name, 'tc': tc, 'password': password, 'password2': password}
        try:
            registration = requests.post(url=register_url, data=data).json()
            if 'errors' in registration:
                errors = registration['errors']
                print(errors)
            elif not 'errors' in registration:
                self.login(email, password)
                print(registration)
                return registration
        except Exception as e:
            print("Something Wrong while register")
    
    def profile(self):
        profile_url = 'https://register-manager.herokuapp.com/api/user/profile'
        headers = {'accept': 'application/json', 'authorization': "Bearer "+ self.access}
        
        user_profile = requests.get(url=profile_url, headers=headers).json()
        print('profile : '+str(user_profile))
        
        


user = API_Cliant()
# user.login()


user.register(name='anwar', email='anwar@gmail.com', tc=True, password='11223344', password2='11223344')
user.profile()
"""
all ok, login register and profile
"""