#!/usr/bin/env python2
# coding=utf-8
import sys
import json
import urllib2

def queryurl(word):
    baseurl = 'http://dict.qq.com/dict?q='
    return baseurl + word

def getpage(url):
    request = urllib2.Request(url)
    page = urllib2.urlopen(request)
    return page

def local_dict(data):
    for local in data['local']:
        for des in local['des']:
            if type(des) is dict:
                print(des['p'] + ' ' + des['d'])
            else:
                print(des)

def get_data(page):
    data = page.read()
    data = json.loads(data)
    return data

def net_dict(data):
    print('Local dict not this word, but network dict had.')

def main():
    page = getpage(queryurl(sys.argv[1]))
    if page.code is not 200:
        raise RuntimeError('Network error.')
    data = get_data(page)
    if 'err' in data:
        print(data['err'])
    elif 'local' in data:
        local_dict(data)
    elif 'netdes' in data:
        net_dict(data)
    else:
        raise RuntimeError('Unknown error in load dict data.')

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        raise ValueError('Please type one word.')
    main()
