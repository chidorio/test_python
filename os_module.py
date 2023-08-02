import os
from datetime import datetime

os.chdir('/Users/GG/Desktop/')

print(os.environ.get('APPDATA'))

# file_path = os.path.join(os.environ.get('APPDATA'), 'test.txt')
# print(file_path)

print(os.path.exists('/tmp/text.txt'))
# for dirpath, dirnames, filenames in os.walk('/Users/GG/Desktop/'):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print()

# mod_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.listdir())
