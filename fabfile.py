# from fabric import Connection
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

host = os.getenv('HOSTS')

print(host)
# c = Connection(host=host, user='ubuntu')
# result = c.run('uname -s')
