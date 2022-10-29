import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('./firebase-sdk.json')
firebase_admin.initialize_app(cred)

# create a user
#'''
email = input('Enter your email  >> ')
password = input('Enter your password >> ')

user = auth.create_user(email = email, password = password)

print('User created successfully : {0}'.format(user.uid))
#'''


# get a user
'''
email = 'test2@gmail.com'

user = auth.get_user_by_email(email)

print('User id is : {0}'.format(user.uid))
'''

# list all the users
'''
page = auth.list_users()

while page:
    for user in page.users:
        print('User: ' + user.uid)

    # get next page
    page = page.get_next_page()
'''