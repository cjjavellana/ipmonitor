#! /usr/bin/env python2.7

'''
Created on Aug 9, 2013

@author: Christian
'''

from ipmonitor.router.AzTech import DSL1015EW
from ipmonitor.github.GitHubUpdater import GitHubUpdater
import os

def main():
    print("Interrogating IP Address from DSL1015EW")
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
        print 'Router\'s Ip has not changed'
    
    
def has_ip_changed(new_ip_address):
    '''
    Checks whether the router's ip address has changed
    '''
    
    if not os.path.exists('ipaddress'):
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
        
        if ipaddress != new_ip_address:
            return True
    
    return False
    
if __name__ == '__main__':
    main()