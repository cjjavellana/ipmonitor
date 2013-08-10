#! /usr/bin/env python2.7

'''
Created on Aug 9, 2013

@author: Christian
'''

import os
from ipmonitor.router.AzTech import DSL1015EW
from ipmonitor.github.GitHubUpdater import GitHubUpdater
import logging

module_logger = logging.getLogger('ipmonitor.main')

def init_logging():
    logger = logging.getLogger('ipmonitor')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('ipmonitor.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
def main():
    module_logger.info('Interrogating IP Address from DSL1015EW')
    router = DSL1015EW()
    
    if has_ip_changed(router.get_external_ip()):
        props = {}    
        with open("github_credentials") as f:
            for line in f:
                if line == '': continue
                val = line.strip().split("=")
                props[val[0]] = val[1] 
        f.close()
    
        g = GitHubUpdater()
        g.login(props['username'].encode('utf-8'), props['password'].encode('utf-8'))
        g.updateServiceHook(router.get_external_ip())
    else:
        module_logger.info('Router\'s Ip has not changed')
    
    
def has_ip_changed(new_ip_address):
    '''
    Checks whether the router's ip address has changed
    '''
    
    module_logger.info('Checking if Ip Address has Changed')
     
    if not os.path.exists('ipaddress'):
        module_logger.info('File ipaddress does not exist yet, creating one now')
        f = file('ipaddress', 'w+')
        f.write(new_ip_address)
        f.close()
        return True
    else:
        ipaddress = ''
        with open('ipaddress') as f:
            for line in f:
                ipaddress = line.strip() 
        f.close();
        
        module_logger.info('Previous Ip Address: ' + ipaddress + ' New Ip Address: ' + new_ip_address)
        
        if ipaddress != new_ip_address:
            return True
    
    return False
    
if __name__ == '__main__':
    init_logging()
    main()