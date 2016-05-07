#-*-coding:utf-8 -*-

import ConfigParser
import os
import log


def getConfig(section, key, filename='info.conf'):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + os.sep + filename
    config.read(path)
    try:
        result = config.get(section, key)
        if result.lower() == str(True).lower():
            result = True
        elif result.lower() == str(False).lower():
            result = False
        return result
    except Exception, e:
        log.Log().sdebug(e)
        return None


if __name__ == '__main__':
    result = getConfig('global', 'FILERECIVER')
    print type(result)
    print type(True)
