## Web Crawler -- A replacement of Scrapy

About 2 years ago, I build my first app using scrapy and PHP. But I used to think it is too complex for me to use.

Later on, I pivoted to requests & Beautifulsoup, which are much more easier for http requests and regex.

However, the scrapy is based on Twisted, which makes scrapy faster than requests & Beautifulsoup.

So, Here's a lib for web crawling. It is based on gevent, requests and Beautifulsoup. It should be faster than requests single processing.(but it need more tests)

The Usage is quite SIMPLE, which is the common character of my piece.

## Usage 

The ```example.py``` is a simple example. the result has been put on [This Site](http://blog.askfermi.me/newsfeed.html).

### Build your model

You have to make a model including required info, as in the example, I have make serveral props and a ```setprops``` method.

In this example, it stores the data into leancloud, if you need to save it to database, just override ```save``` method.

### Write Extractor

You need to build your own extractor, which is the rule how spider extract information from website. it uses Beautifulsoup to extract.

In the Extractor, you will need to fulfill the model and call it's save method.

## More 

The Performance test will be a key point in the future development.

Graphite will be added soon for visualization.