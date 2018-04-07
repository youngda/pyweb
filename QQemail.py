#coding:utf-8  
import smtplib 
import requests
import json
import time
from email.mime.text import MIMEText  
from email.header import Header  
  
# 第三方 SMTP 服务  
mail_host="smtp.qq.com"  #设置服务器  
mail_user="1217882800@qq.com"    #用户名  
mail_pass="jlberv********ic"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得,不含空格  
  
  
sender = '1217882800@qq.com'  
receivers = ['1217882800@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱  
  
message = MIMEText('积分用完', 'plain', 'utf-8')  
message['From'] = Header("youngda", 'utf-8')  
message['To'] =  Header("myself", 'utf-8')  
  
subject = '积分用完，充值'  
message['Subject'] = Header(subject, 'utf-8')
url = "https://wenkubao.cc/?GetScore&id=ax444&pw=zaw6&t=1523010045165"
mark = 1

while mark == 1:
    res = requests.get(url)
    jsonstr = json.loads(res.text)
    if jsonstr['score'] <=10:
        try:
          smtpObj = smtplib.SMTP_SSL(mail_host, 465)   
          smtpObj.login(mail_user,mail_pass)    
          smtpObj.sendmail(sender, receivers, message.as_string())  
          smtpObj.quit()  
          print (u"邮件发送成功")
          mark = 0
        except smtplib.SMTPException as e:  
          print (e)
    time.sleep(60)
    print(jsonstr['score'])
print("over")
