# ! /usr/bin/python2.7
# coding=utf-8
import requests
import re
import json
import urllib
import sys


def echoDownloader(url):

    #获取网站的内容
    res = requests.get(url)

    # 正则匹配出关键字符串
    res = re.findall('var page_sound_obj =(.+)', res.text)

    #构造json格式数据
    res = res[0].replace(';', '')

    # 解析json格式数据
    res = json.loads(res)

    title = res['name']
    url = res['source']

    # 下载mp3
    urllib.urlretrieve(url, title + ".mp3")


if __name__ == '__main__':
    if len(sys.argv)==2:
        echoDownloader(sys.argv[1])
        pass
    else:
        print "输入格式不正确"
