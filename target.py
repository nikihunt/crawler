#-*-coding:utf-8 -*-

import requests
import ConfigParser
import os


class Target(object):
    """target represent something the spider will crawle"""

    def __init__(self):
        self.resp = ''  # response obj
        self.formhash = ''  # you will need formhash when replying the post
        self.formhash_pattern = re.compile(
            r'<input type="hidden" name="formhash" value="([0-9a-zA-Z]+)" />')

    def login(self, username, passwd, questionid=0, answer=''):
        post_data = {
            'loginfield': config.LOGINFIELD,
            'username': username,
            'password': password,
            'questionid': questionid,
            'answer': answer,
            'cookietime': config.COOKIETIME,
        }
