#! /usr/bin/env python2.7

'''
Created on Aug 9, 2013

@author: Christian
'''

from ipmonitor.router.AzTech import DSL1015EW

def main():
    print("Interrogating IP Address from DSL1015EW")
    router = DSL1015EW()
    print router.get_external_ip()
    
if __name__ == '__main__':
    main()