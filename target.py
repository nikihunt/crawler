#-*-coding:utf-8 -*-

import requests
import ConfigParser
import os
import config
import log


class Target(object):
    """target represent something the spider will crawle"""

    def __init__(self):
        self.resp = ''  # response obj
        self.formhash = ''  # you will need formhash when replying the post
        self.formhash_pattern = re.compile(
            r'<input type="hidden" name="formhash" value="([0-9a-zA-Z]+)" />')

        self.log = log.Log()

    def getResponse(self, url, data=None):
        if url == '' or url == None:
            self.log.swaring('url is null')
            return None
        else:
            header = config.getConfig('USERAGENT')
            try:
                req = requests.post(url, data, headers=header)
            except Exception, e:
                self.log.#-------------------------------------------------------------------------------
            finally:
                pass

    def login(self, username, passwd, questionid=0, answer=''):
        post_data = {
            'loginfield': config.LOGINFIELD,
            'username': username,
            'password': password,
            'questionid': questionid,
            'answer': answer,
            'cookietime': config.COOKIETIME,
        }
        login_success_pattern = re.compile(
            ur"\('succeedlocation'\).innerHTML = '(?u)(.+)，现在将转入登录前页面';")
        login_fail_pattern = re.compile(
            r"{errorhandle_\('(?u)(.+)', {'loginperm':")
