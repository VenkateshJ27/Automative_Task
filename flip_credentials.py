import os
os.environ['EMAIL_'] = 'venkatesh.27091998@gmail.com'
os.environ['PASS_'] = '416061061'
os.environ['PHONE_'] = '9620223549'

email_ = 'EMAIL_'
email_id = os.environ.get(email_, 'Email id not present')

password_ = 'PASS_'
pass_ = os.environ.get(password_, 'Password not present')

phoneno_ = 'PHONE_'
phone_ = os.environ.get(phoneno_, 'Phone Number not present')


















# email_id = os.environ['EMAIL_']
# password_ = os.environ['PASS_']
# phone_no = os.environ['PHONE_']


# print(f'{email_id} home directory is {password_} and {phone_no}')


# for k,v in os.environ.items():
#     print(f'{k}={v}')











# print(os.environ)
# print(os.environ.get('USER'))

# home_dir = os.environ['U']
# username = os.environ['K']
# print(f'{username} home directory is {home_dir}')

# os.environ['U'] = 'H'

# os.environ.pop('U')
# os.environ.clear