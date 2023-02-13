from selenium import webdriver

import random
import string

def email_generate():
    prefix=''.join(random.choice(string.ascii_lowercase) for i in range(4))
    domain=''.join(random.choice(['gmail','yahoo','outlook']))
    suffix=''.join(random.choice(['com','net','org','edu']))
    print(prefix+'@'+domain+'.'+suffix)

email_generate()