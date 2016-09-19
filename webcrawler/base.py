#coding:utf-8
'''
@Author: Xiaozhe Yaoi <i@askfermi.me>
'''
from gevent import monkey; monkey.patch_socket()
import gevent
import requests
from bs4 import BeautifulSoup


class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  



'''
Base Spider defines the crawling site using requests.
'''
class BaseSpider(Singleton):
    def __init__(self,url):
        self.url=url
    def crawl(self):
        '''
        rewrite this method to support get & post method.
        '''
        r=requests.get(self.url)
        return r.text

class BaseExtractor():
    def __init__(self):
        pass
    def setContent(self,content):
        self.soup=BeautifulSoup(content)
    def select(self,stat):
        return self.soup.select(stat)
    '''
    Override this method to implements different extract
    '''
    def extract(self):
        pass

'''
Helper Functions
'''
def crawl(url,extractor):
    crawler = BaseSpider(url)
    text=crawler.crawl()
    extractor.setContent(text)
    extractor.extract()

class CrawlerFactory():
    def start(self,urls,extractor):
        for url in urls:
            threads = []
            for i in range(1,2):
                threads.append(gevent.spawn(crawl, url,extractor))
            gevent.joinall(threads)
        print 'Finished'