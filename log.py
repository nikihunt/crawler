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

        # shi fou jiang log da yin dao zhongduan(ru ping mu)
        self.terminal = True
        self.file = False  # shi fou jiang log da yin dao wen jian zhong

    def getCurrentTime(self, TimeFormat="%Y-%m-%d-%X"):
        '''get Current Time with custom formatter'''

        return time.strftime(TimeFormat, time.localtime())

    def setFLogger(self, LogDestination=sys.path[0], LogLevel=logging.NOTSET):
        '''set file log with default value,sys.path[0] is the current file's dict'''

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
        '''set Stream Log with custom formatter'''
        self.slogger = logging.getLogger()
        logHandler = logging.StreamHandler()
        self.slogger.addHandler(logHandler)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        logHandler.setFormatter(formatter)
        self.slogger.setLevel(LogLevel)

    def setSLoggerLevel(self, LogLevel=logging.NOTSET):
        '''set stream log level,you must check whether the slogger is null'''
        if self.slogger != '':
            self.slogger.setLevel(LogLevel)

    def setFLoggerLevel(self, LogLevel=logging.NOTSET):
        '''set file log level,you must check whether the flogger is null'''
        if self.flogger != '':
            self.flogger.setLevel(LogLevel)

    def setReciver(self, terminal, fileR):
        '''set the log reciver(terminal,file)'''
        self.terminal = terminal
        self.file = fileR

    def debug(self, message=None):
        '''debug and print the message to reciver, you should check the logger whether is null'''
        if self.slogger == '':
            self.setSLogger()
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        if self.terminal:
            self.slogger.debug(message)
        if self.file:
            self.flogger.debug(message)

    def info(self, message=None):
        if self.slogger == '':
            self.setSLogger()
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        if self.terminal:
            self.slogger.debug(message)
        if self.file:
            self.flogger.debug(message)

    def waring(self, message=None):
        if self.slogger == '':
            self.setSLogger()
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        if self.terminal:
            self.slogger.debug(message)
        if self.file:
            self.flogger.debug(message)

    def error(self, message=None):
        if self.slogger == '':
            self.setSLogger()
        if self.flogger == '':
            self.setFLogger()
        if message == None:
            message = self.defaultlog
        if self.terminal:
            self.slogger.debug(message)
        if self.file:
            self.flogger.debug(message)

    def test(self):
        self.debug("this is flogger debug")
        self.info("this is flogger info")
        self.waring("this is flogger warning")
        self.error("this is flogger error")

if __name__ == '__main__':
    Log().test()
