#coding:utf-8
'''
@Author: Xiaozhe Yaoi <i@askfermi.me>
'''

import leancloud
from costina.basemodel import Model,StringField
from costina.base import BaseExtractor,CrawlerFactory
import urllib
import jieba.analyse
import jieba


class Article(Model):
    link=StringField('link')
    title=StringField('title')
    source=StringField('source')
    keyword=StringField('keyword')
    def __init__(self):
        pass
    def setProps(self,link,title,source,keyword):
        self.link=link
        self.title=title
        self.source=source
        self.keyword=keyword
    def add(self):
        try:
            self.save()
        except Exception,e:
            print str(e)

class CBExtract(BaseExtractor):
    def extract(self):
        rs_link=[a.attrs.get('href') for a in self.select('h4 a[target^=_blank]')]
        rs_name=[a.get_text() for a in self.select('h4 a[target^=_blank]')]
        for index,item in enumerate(rs_link):
            article=Article()
            url=item
            try:
                start = item.index('url=')+4
                stop = item.index('aid')-1
                url=urllib.unquote(item[start:stop])
                print item[start:stop]
                tags = jieba.analyse.extract_tags(rs_name[index], topK=5)
                keyword="|".join(tags)
                article.setProps(url,rs_name[index],'manongio',keyword)
                article.save()
                print 'ok'
            except Exception,e:
                print str(e)

def main():
    leancloud.init("APP_ID", "APP_KEY")
    cbe=CBExtract()
    urls=['http://weekly.manong.io/issues/137']
    cf=CrawlerFactory()
    cf.start(urls,cbe)

if __name__=='__main__':
    main()