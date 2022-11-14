import requests

class API_Cliant():
    def __init__(self, refresh='', access=''):
        self.refresh = refresh
        self.access = access
        
    def login(self, email, password):
        login_url = 'http://127.0.0.1:8000/api/user/login' # 'https://register-manager.herokuapp.com/api/user/login' 
        headers = {'accept': 'application/json'}
        credentials = {"email": email, "password": password}
        try:
            user_login = requests.post(url=login_url, headers=headers, data=credentials).json()
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
        register_url = 'http://127.0.0.1:8000/api/user/register' # 'https://register-manager.herokuapp.com/api/user/register' #
        data = {'email': email, 'name': name, 'tc': tc, 'password': password, 'password2': password2}
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
        profile_url = 'https://register-manager.herokuapp.com/api/user/profile' #'http://127.0.0.1:8000/api/user/profile' #
        headers = {'accept': 'application/json', 'authorization': "Bearer "+ self.access}
        try:
            user_profile = requests.get(url=profile_url, headers=headers).json()
            if 'errors' in user_profile:
                errors = user_profile['errors']
                print(errors)
            elif not 'errors' in user_profile:
                print('profile : '+str(user_profile))
        except Exception as e:
            print('Something wrong while getting profile')

    def change_password(self, password, password2):
        changepassword_url = 'https://register-manager.herokuapp.com/api/user/changepassword' #'http://127.0.0.1:8000/api/user/changepassword' #
        headers = {'accept': 'application/json', 'authorization': "Bearer "+ self.access}
        data = {'password': password, 'password2': password2}
        try:
            changepassword_call = requests.post(url=changepassword_url, headers=headers, data=data).json()
            if 'errors' in changepassword_call:
                errors = changepassword_call['errors']['non_field_errors']
                print(errors)
            elif not 'errors' in changepassword_call:
                message = changepassword_call['message']
                print(message)
        except Exception as e:
            print('Something wrong while change password')
        print('Change Passeord: '+ str(changepassword_call))
    
    def reset_password_request(self, email):
        resetpassword_url = 'https://register-manager.herokuapp.com/api/user/send-password-reset-email' #'http://127.0.0.1:8000/api/user/send-password-reset-email' #
        headers = {'accept': 'application/json'}
        data = {'email': email}
        try:
            reset_password = requests.post(url=resetpassword_url, headers=headers, data=data).json()
            if 'errors' in reset_password:
                errors = reset_password['errors']['non_field_errors']
                print(errors)
            elif not 'errors' in reset_password:
                message = reset_password['message']
                print(message)
        except Exception as e:
            print('Something wrong while reset_password_request')

    def reset_password(self, password, password2):
        reset_url = 'http://127.0.0.1:8000/api/user/reset-password/MTQ/bevmwg-60585182865ed6673c87b3aae93d547e'
        headers = {'accept': 'application/json'}
        data = {'password': password, 'password2': password2}
        reset_password = requests.post(url=reset_url, headers=headers, data=data).json()
        print(reset_password)

user = API_Cliant()
user.register(name='mizan', email='mizan.electronics11@gmail.com', tc=True, password='11223344', password2='11223344')

# user.login(email='mizan.electronics11@gmail.com', password='1111222')
# user.profile() # need login() call
# user.change_password(password='11223344', password2='11223344') # need login() call
# user.reset_password_request(email='mizan.electronics11@gmail.com')
# user.reset_password(password='11112222', password2='11112222') # No need this cause this section is browseable