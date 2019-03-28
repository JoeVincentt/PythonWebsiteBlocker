import time
from datetime import datetime as dt

# Windows Settings
host_path = r"C:\Windows\System32\drivers\ect\hosts"
# Mac or Linux Settings
# host_path = r"/ect/hosts"
redirect = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working hours..')
    else:
        print('Fun hours..')
    time.sleep(5)