# -*- coding:utf-8 -*-
import urllib
import MySQLdb
import cal_dis as calculate
#fp=open("data.txt","r")

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='19970615',
        db ='aaa',
        charset='utf8'
        )

conn.set_character_set('utf8')


cur = conn.cursor()
cur.execute('SET NAMES utf8;')
cur.execute('SET CHARACTER SET utf8;')
cur.execute('SET character_set_connection=utf8;')

sql="select * from dust LIMIT 100"
cur.execute(sql)
result=cur.fetchall()
#print result
lng=116.402
lat=39.9
list1=[]#存储距离
list2=[]#存储地名
list3=[]#中间过渡进行unicode转utf-8
list_ing=[]
list_lat=[]
fp=open('places.txt','a')
for row in result:
        #fp.write(row[0]. encode('utf-8')+'\t'+str(row[1])+'\t'+str(row[2])+'\n')
        list2.append(row[0])
        list_ing.append(row[1])
        list_lat.append(row[2])
        #print row[1],row[2]
        list1.append(calculate.calcDistance(lat,lng,row[2],row[1]))#存储距离
# SQL 插入语句

location=[]
list_i=[]
list_l=[]
for x in range(0,len(list1)):
        if list1[x]<5.0:#距离小于10
                list3.append(list2[x])
                list_i.append(list_ing[x])
                list_l.append(list_lat[x])

#print list3

list4=[]#存储最终的输出景点
for line in list3:
        line1=line.encode('utf-8')
        list4.append(line1)
           # 提交到数据库执行
        #print line1
print len(list4)
for x in range(len(list4)):
    fp.write(list4[x]+'\t'+str(list_i[x])+'\t'+str(list_l[x])+'\n')
conn.commit()
fp.flush()
fp.close()


conn.close()
