'''
Created on Aug 9, 2013

@author: Christian
'''

import urllib2
import json
from ipmonitor.json.JsonUtil import _decode_dict

'''
The class for interrogating an aztech router model DSL1015EW
'''
class DSL1015EW:
    
    def __init__(self):
        response = urllib2.urlopen('http://192.168.1.254/main_json.html')
        str_response = response.read().encode('utf-8').replace('\n', '') \
            .replace('{', '{"')    \
            .replace(':\'', '":"') \
            .replace('\',', '","') \
            .replace('\'', '"')  
    
        self.json_obj = json.loads(str_response, object_hook=_decode_dict)

            
    def get_external_ip(self):
        return self.json_obj['wanipaddress']
