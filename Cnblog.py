#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpc.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
config = {
    'url':    'https://rpc.cnblogs.com/metaweblog/YoSaukit',
    'appKey': 'YoSaukit',
    'user':   'YoSaukit',
    'passwd': 'mqiuqiu1988!'
}

class MetaWeblog:
    def __init__(self, url, appKey, user, passwd):
        self.url, self.appKey, self.user, self.passwd = url, appKey, user, passwd
        self.proxy = xmlrpc.client.ServerProxy(self.url)


    def getRecentPosts(self, blogid='', count=5):
        return self.proxy.metaWeblog.getRecentPosts(blogid, self.user, self.passwd, count)

if __name__ == '__main__':
    weblog = MetaWeblog(**config)
    print(weblog.getRecentPosts())