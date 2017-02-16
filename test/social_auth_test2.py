from social_auth.facebook.authentication import login

username=raw_input('Enter Username:')
password=raw_input('Enter password:')

login(username,password)
