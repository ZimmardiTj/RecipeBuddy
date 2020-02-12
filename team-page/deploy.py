import os
import sys

def deploy(username):
  os.system("scp index.html " + username + "@maphey.com:/var/www/html/cs350.maphey.com/")

if __name__ == "__main__":
  deploy(sys.argv[1])
