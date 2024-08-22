import urllib
import urllib.request
try:
          site = urllib.request.urlopen('https://www.instagram.com/')
except:
        print('\033[0;31mNão foi possível acessar o site.\033[m')
else:
        print('\033[0;32mConsegui acessar o site!\033[m')