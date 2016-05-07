#-*- coding: utf-8 -*-

import os
import sys
import logging
import time


class Log(object):

    def __init__(self):
        self.slogger = ''
        self.flogger = ''
        self.defaultlog = 'this is default log info'
        self.terminal = True
        self.file = False

    # 获取当前时间
    def getCurrentTime(self, TimeFormat="%Y-%m-%d-%X"):
        return time.strftime(TimeFormat, time.localtime())

    # 设置log,sys.path[0]为当前脚本所在目录
    def setFLogger(self, LogDestination=sys.path[0], LogLevel=logging.NOTSET):
        self.flogger = logging.getLogger()
        dirpath = LogDestination + os.sep + self.getCurrentTime("%Y-%m-%d")
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        # 不能用getCurrentTime("%X")，因为%X格式（h:m:s）中带有":"符号，而文件名中不能出现该符号
        LogDestination = dirpath + os.sep + self.getCurrentTime("%H") + ".log"
        logHandler = logging.FileHandler(LogDestination)

        self.flogger.addHandler(logHandler)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logHandler.setFormatter(formatter)
        self.flogger.setLevel(LogLevel)

    def setSLogger(self, LogLevel=logging.NOTSET):
        self.slogger = logging.getLogger()
        logHandler = logging.StreamHandler()
        self.slogger.addHandler(logHandler)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logHandler.setFormatter(formatter)
        self.slogger.setLevel(LogLevel)

    def setSLoggerLevel(self, LogLevel=logging.NOTSET):
        self.slogger.setLevel(LogLevel)

    def setFLoggerLevel(self, LogLevel=logging.NOTSET):
        self.flogger.setLevel(LogLevel)

    def setReciver(self, terminal, fileR):
        self.terminal = terminal
        self.file = fileR

    def debug(self, message=None):
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        self.flogger.debug(message)

    def info(self, message=None):
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        self.flogger.info(message)

    def waring(self, message=None):
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        self.flogger.warning(message)

    def error(self, message=None):
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        self.flogger.warning(message)

    def test(self):
        self.fdebug("this is flogger debug")
        self.finfo("this is flogger info")
        self.fwaring("this is flogger warning")
        self.ferror("this is flogger error")

if __name__ == '__main__':
    Log().test()
