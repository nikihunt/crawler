#-*-coding:utf-8 -*-

import ConfigParser
import os
import log


def getConfig(section, key, filename='info.conf'):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + os.sep + filename
    config.read(path)
    try:
    	return config.get(section, key)
    except Exception, e:
    	log.Log().sdebug(e)
    finally:
    	return None


if __name__ == '__main__':
    print getConfig(None,None)
