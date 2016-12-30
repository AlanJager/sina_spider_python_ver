# sina_spider_python_ver
=========================
[![Build Status](https://travis-ci.org/AlanJager/sina_spider_python_ver.png)](https://travis-ci.org/AlanJager/sina_spider_python_ver)
![](https://github.com/AlanJager/sina_spider_python_ver/blob/master/icon.png)

A sina weibo crawler based on python scrapy

Features
--------
* Support git/svn Version control system.
* Customize information class (but should be weibo information)
* HTTP error handle
* MongoDB support
* Multi threads supprot
* Distribute deployment available

Requirements
------------

* Bash(git, ssh/zsh)
* Python 2.7
* Scrapy

Installation
------------
```
git clone https://github.com/AlanJager/sina_spider_python_ver
cd sina_spider_python_ver
python Begin.py

```

Quick Start
-------------

* ....


Custom
--------
if you need to custom it for yourself

* Add new request
    ```python
    vi spiders/spiders.py
    
    def parse3(self, response):
        items = response.meta["item"]
        selector = Selector(response)
    ```

* Add new items
    ```python
    vi items.py

    class FollowsItem(Item):
        _id = Field()  
        follows = Field() 
    ```

* Add new middleware
    ```php
    vi middleware.py

    class UserAgentMiddleware(object):
        def process_request(self, request, spider):
            agent = random.choice(agents)
            request.headers["User-Agent"] = agent
            ....       
    
    :wq
   
    vi settings.py
    
    DOWNLOADER_MIDDLEWARES = {
        "Sina_spider.middleware.UserAgentMiddleware": 401,
        "Sina_spider.middleware.CookiesMiddleware": 402,
    }
    ```

To Do List
----------

- Travis CI integration
- Resolve 301 code

Update
-----------------



Architecture
------------

## CHANGELOG
[CHANGELOG](https://github.com/AlanJager/sina_spider_python_ver/releases)


Discussing
----------
- [submit issue](https://github.com/AlanJager/sina_spider_python_verissues/new)
- email: msjdxhc@gmail.com

