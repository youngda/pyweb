
# coding: utf-8

# In[71]:


import requests

headers = {
    "Accept": "application/json",
    "Accept-Charset":"utf-8",
    "Accept-Encoding":"gzip, deflate",
    "User-Agent":"IFTTT-Protocol/v1",
    "Authorization":"Bearer 5ba3edf09d394498f91ce456213db8f1",
    "X-Request-ID":"80b3fa12814d4e9dba67b2ccb85b6d86"
}
res = requests.get("http://xxxxx.xxit.am/echo/ifttt/ifttt/v1/user/info",headers = headers)
print(res.text)
print(res.headers)

