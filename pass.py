#百度文库账号：xxnmc        密码：62585  
# https://wenkubao.cc  
import requests
import bs4
class RePass(object):
    def __init__(self):
        self.headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Length":"66",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":"rememberUser=true; userName=xxnmc; passWord=62585",
            "Host":"wenkubao.cc",
            "Origin":"https://wenkubao.cc",
            "Referer":"https://wenkubao.cc/edit.aspx",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        self.session = requests.session()
    def login(self,username,oldpassword,repassword):
        login_url = 'https://wenkubao.cc/edit.aspx'

        data = {"username":username,
                "oldpwd":oldpassword,
                "userpwd":repassword,
                "userpwdok":repassword
                }
        self.session.post(login_url,data=data,headers = self.headers)
        return repassword
if __name__ == '__main__':
    username = 'xxnmc'
    repasswd = 1
    D  = RePass()
    oldpass = "11110000"
    while repasswd<100:
        strpass = "hello"+str(repasswd)
        repasswd = repasswd + 1
        intstr = D.login(username,oldpass,strpass)
        oldpass = strpass
        print(strpass)