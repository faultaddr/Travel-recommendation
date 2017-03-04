# -*- coding:utf-8 -*-
import urllib2
import re
import threading
import time
count=0
threads = []
def getjpg(url):
    global count
    response = urllib2.urlopen(url)
    html = response.read()
    #print html
    # 保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
    pattern = re.compile("<img src=\"(.+)\" width=\"220\" height=\"140\"")
    images = re.findall(pattern, html)

    #print images
    for image in images:
        name = "./" + str(count) + ".jpg"
        conn = urllib2.urlopen(image)
        f = open(name, 'wb')
        f.write(conn.read())
        f.close()
        print('Pic Saved!')
        count += 1
def start():

    for x in range(1,179):
        str1="http://you.ctrip.com/sight/beijing1/s0-p"+str(x)+".html"
        t1 = threading.Thread(target=getjpg, args=(str1,))

        threads.append(t1)

    for t in threads:

        #t.setDaemon(True)

        t.start()
        time.sleep(300)
start()