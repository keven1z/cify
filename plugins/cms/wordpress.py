from common.net.url import WrappedUrl
from common.utils.encryption import *
import hashlib
import re
import copy

name = 'Wordpress'
description = "WordPress is an opensource blogging system commonly used as a CMS."


def check(self, wurl):
    index_text = ['<a href="http://www.wordpress.com">Powered by WordPress</a>', '<link rel=\'https://api.w.org/\'']
    if isinstance(wurl, WrappedUrl):
        # 主页判断
        response = self._request(wurl)
        html = response.content
        if isinstance(html, bytes):
            html = str(html, encoding='utf-8')
        for text in index_text:
            res = html.find(text)
            if res != -1:
                match = re.findall('<meta name="generator" content="(WordPress [0-9\.]+)"', html)
                if match is not None:
                    return match[0]
                else:
                    return name
        # 通过常见url判断
    '''
     {: url = > "/wp-cron.php"},

     # {:url=>"/admin/", :full=>true }, # full means that whatweb will run all plugins against this url - this isn't yet implemented as of 0.4.7

     # /wp-login.php  exists & contains a string

     {: url = > "/wp-login.php",: text = > '<a title="Powered by WordPress" href="http://wordpress.org/">'},
     {: url = > "/wp-login.php",: text = > '<a href="http://wordpress.org/" title="Powered by WordPress">',: name = > 'wp3 login page'},
     {: url = > "/wp-login.php",: text = > 'action=lostpassword'},

     {: url = > "/wp-login.php",: tagpattern = > "!doctype,html,head,title,/title,meta,link,link,script,/script,meta,/head,body,div,h1,a,/a,/h1,form,p,label,br,input,/label,/p,p,label,br,input,/label,/p,p,label,input,/label,/p,p,input,input,input,/p,/form,p,a,/a,/p,p,a,/a,/p,/div,script,/script,/body,/html"},  # note that WP plugins can add script tags. tags are delimited by commas so we can count how close it is
     {: url = > "favicon.ico",: md5 = > 'f420dc2c7d90d7873a90d82cd7fde315'},  # not common, seen on http://s.wordpress.org/favicon.ico
     {: url = > "favicon.ico",: md5 = > 'fa54dbf2f61bd2e0188e47f5f578f736',: name = > 'WordPress.com favicon'},  # on wordpress.com blogs  http://s2.wp.com/i/favicon.ico

     {: url = > "/readme.html",: version = > / < h1. * WordPress. * Version([0 - 9a - z\.]+).* < \ / h1 > / m}
     '''
    # 判断 /wp-cron.php 返回值为200
    c_url = copy.deepcopy(wurl)
    c_url.url = c_url.scheme + '://' + c_url.hostname + '/wp-cron.php'
    resp = self._request(c_url)
    if resp.status_code == 200:
        return name

    # 判断 /wp-login.php
    c_url.url = c_url.scheme + '://' + c_url.hostname + '/wp-login.php'
    resp = self._request(c_url)
    if resp.status_code == 200:
        login_text = ['<a title="Powered by WordPress" href="http://wordpress.org/">',
                      '<a href="http://wordpress.org/" title="Powered by WordPress">', 'action=lostpassword']
        response = self._request(wurl)
        html = response.content
        html = str(html, encoding='utf-8')
        for text in login_text:
            res = html.find(text)
            if res != -1:
                return name
    c_url.url = c_url.scheme + '://' + c_url.hostname + '/favicon.ico'
    resp = self._request(c_url)
    content = resp.content

    filemd5 = file2md5(content)
    md5_list = ['f420dc2c7d90d7873a90d82cd7fde315', 'fa54dbf2f61bd2e0188e47f5f578f736',
                '20e22c1aa0fd7ff6a970bd5c207c4794']
    if filemd5 in md5_list:
        return name

    return None
