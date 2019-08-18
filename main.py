import re
import os
import pyperclip
import sys
import time
import random
import string

pattern = sys.argv[1]

prev_string = ''

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def check_text(tmp_string):

    if not re.search(pattern, tmp_string):
        return False

    if tmp_string == prev_string:
        return False

    return True

base_dir = os.getcwd() + 'pastes/'
os.makedirs(base_dir, exist_ok=True)

while True:
    tmp_string = pyperclip.paste()
    if check_text(tmp_string):
        with open(base_dir + randomname(10), mode='w') as f:
            f.write(tmp_string)
            f.close()
            prev_string = tmp_string
            print('paste to file done')

    time.sleep(1)
