import re
from selenium import webdriver
import Queue
import threading
import sys
import time
import random
import os;
class MyThread(threading.Thread):
    def __init__(self, workQueue, resultQueue,timeout=30, **kwargs):
        threading.Thread.__init__(self, kwargs=kwargs)
  #线程在结束前等待任务队列多长时间
        self.timeout = timeout
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.start()

    def run(self):
        while True:
            try:
    #从工作队列中获取一个任务
                callable, args, kwargs = self.workQueue.get(timeout=self.timeout)
    #我们要执行的任务
                res = callable(args, kwargs)
    #报任务返回的结果放在结果队列中
                self.resultQueue.put(" | ")
            except Queue.Empty: #任务队列空的时候结束此线程
                break
            except :
                print sys.exc_info()
        raise

class ThreadPool:
    def __init__( self, num_of_threads=10):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.threads = []
        self.__createThreadPool( num_of_threads )

    def __createThreadPool( self, num_of_threads ):
        for i in range( num_of_threads ):
            thread = MyThread( self.workQueue, self.resultQueue )
            self.threads.append(thread)

    def wait_for_complete(self):
  #等待所有线程完成。
        while len(self.threads):
            thread = self.threads.pop()
   #等待线程结束
            if thread.isAlive():#判断线程是否还存活来决定是否调用join
                thread.join()

    def add_job( self, callable, *args, **kwargs ):
        self.workQueue.put( (callable,args,kwargs) )

def test_job(id,sleep=0.001,str1='',str2=''):
    #print "start-->>"
    #browser = webdriver.Chrome('C:\Users\panda\Desktop\chromedriver.exe') # Get local session of firefox
    proxy=[]
    fp=open("ip.txt",'r')
    for line in fp.readlines:
        proxy.append("\""+line+"\"")
    print proxy
    service_args = [
 '--proxy='+proxy[random.randint(0,100)],
 '--proxy-type=socks5',
 ]
    browser=webdriver.PhantomJS(service_args=service_args)
    #browser.get(r'http://pansijian.haodf.com/') # Load page


    browser.get(str1)
    response = browser.page_source.encode('utf-8')

    #print "get-->>"
    #time.sleep(0.5)

    #print "click-->>"
    #time.sleep(0.5) # Let the page load, will be added to the API
    browser.close()
    #browser.quit()
    return response
def getdata(self,response):
    pattern_jpg=re.compile(r"<img (.+) width='220'",re.S)
    jpg_url=re.findall(pattern_jpg,response)

    for pic_url in jpg_url:
        loadPicture(pic_url, path)
        count = count + 1
def loadPicture(pic_url, pic_path):
    pic_name = os.path.basename(pic_url) #delete path, get the filename
    urllib.urlretrieve(pic_url, pic_path + pic_name)
def test(str1='',str2=''):
    '''
    print "Instruction\n"
    print"please input the time that you want to click,and then you will see\n"
    print"how many times do you want to add  then you should input an Integer\n"
    print"then you will see start testing---->>>>and then the proceduce last for\n"
    print"several minutes so keep calm and wait for the 'end testing' then you can\n"
    print"close it"
    '''
    count=0
    #a=input("how many times do you want to add  ")
    print 'start testing'
    tp = ThreadPool(10)
    for i in range(50):
        time.sleep(0.2)
        tp.add_job( test_job, i, i*0.001,str1,str2 )
        count+=1
        #print "Click "+str(count)+" time(s) \n"
        #print "please wait for 'end testing'\n"
    tp.wait_for_complete()
    #print 'result Queue\'s length == %d '% tp.resultQueue.qsize()
    #print count
    while tp.resultQueue.qsize():
        print tp.resultQueue.get()
    #print 'end testing'
