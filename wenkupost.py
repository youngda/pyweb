
# coding: utf-8

import requests
import base64
url = 'http://139.224.236.108/post.php'
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "51",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "qualityawarddialog=yes; BAIDUID=414377076CD277B17F797E7A9E8E11FE:FG=1; BIDUPSID=414377076CD277B17F797E7A9E8E11FE; PSTM=1504154629; __cfduid=d78fc8eee8818c92340cfd604969246861504181925; _click_param_pc_rec_doc_2017_testid=2; MCITY=-%3A; isJiaoyuVip=1; LoseUserAllPage=%7B%22status%22%3A0%2C%22expire_time%22%3A0%2C%22create_time%22%3A1522306153%2C%22type%22%3A0%2C%22cookie_time%22%3A1522565353%7D; H_PS_PSSID=1469_18195_21114_20930; PSINO=7; cflag=15%3A3; FP_UID=6d9a26be8a9f7485b6bcc213ac6471f4; BDUSS=XVNfkUzcjAxaTlYTnpIfkt3dmNuUXZvUlYwT2pvYjRhbUhJSmRXTmpXOU9PdVZhQVFBQUFBJCQAAAAAAAAAAAEAAABE67q2YmVtZmFfY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE6tvVpOrb1ab; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1522380846; Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6=1522380846",
    "Host": "139.224.236.108",
    "Origin": "http://139.224.236.108",
    "Referer": "https://wenku.baidu.com/view/40031cea5ef7ba0d4a733b90.html?from=search",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
data = {
    "usrname": "rpu6kv",
    "usrpass": "cx83zu",
    "docinfo": "6d44f96a581b6bd97e19ea14",
    "taskid": "up_down_doc",
}
res = requests.post(url,data=data,headers = headers)
res.encoding = 'UTF-8'
get_code = res.text
print(res.text)
get_code = get_code.split("----")
print(base64.b64decode(get_code[0]).decode())
print(get_code[1])

