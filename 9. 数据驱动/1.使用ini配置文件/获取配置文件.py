#! /usr/bin/env python
# author: vin

import configparser

def getConfig():
    list_config = []
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config.get(config.sections()[0], 'host')
    port = config.get(config.sections()[0], 'port')
    username = config.get(config.sections()[0], 'username')
    password = config.get(config.sections()[0], 'password')
    list_config.append(host)
    list_config.append(port)
    list_config.append(username)
    list_config.append(password)
    return list_config

print(getConfig())