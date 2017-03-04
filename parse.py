# -*- coding:utf-8 -*-
import urllib
import MySQLdb
import  re
import time
fp=open("data.txt","r")

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='19970615',
        db ='aaa',
        charset='utf8'
        )

conn.set_character_set('utf8')


for line in fp.readlines():
    cur = conn.cursor()
    cur.execute('SET NAMES utf8;')
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('SET character_set_connection=utf8;')
    line=line.split("\n")[0]
    #print line
    str1="http://api.map.baidu.com/geocoder/v2/?output=json&address="+line+"&city=北京市&ak=ajdvwjjvP1LRwfFsTVZo0uFrm8duuUci"
    #print str1

    try:
        f = urllib.urlopen(str1)
        s = f.read()
    except Exception:
        continue
    print s
    pattern=re.compile("lat")
    list1=re.findall(pattern,s)
    if(list1!=None):
        s = eval(s)
    else:
        continue
    if(s['status']==0):

        dict1=s['result']
        dict2=dict1['location']
        lng=dict2['lng']

        lat=dict2['lat']
        print line
# 打开数据库连接


# 使用cursor()方法获取操作游标
        cursor =conn.cursor()

# SQL 插入语句
        sql = "INSERT INTO location(sight, \
           lng, lat) \
           VALUES ('%s', '%f', '%f')" % \
           (line.decode('utf-8'),lng,lat)

        cursor.execute(sql)
           # 提交到数据库执行
        conn.commit()

    else:
        continue
# 关闭数据连接

conn.close()
