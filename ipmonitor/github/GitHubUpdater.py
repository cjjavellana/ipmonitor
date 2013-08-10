'''
Created on Aug 9, 2013

@author: Christian
'''

from github import Github
import logging

module_logger = logging.getLogger('ipmonitor.githubupdater')

class GitHubUpdater:
    '''
    classdocs
    '''
    
    HOOK_ID = 1176921
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def login(self, username, password):
        '''
        Login
        '''
        g = Github(username, password)
        self.repo = g.get_user().get_repo("aia")
        
        
    def updateServiceHook(self, new_ip_address):
        '''
        Update Service Hook
        '''
        new_url = 'http://' + new_ip_address + ':8083/github-webhook/'
        
        module_logger.info('Updating Jenkins Hook Url to ' + new_url)
        
        jenkins_hook = self.repo.get_hook(self.HOOK_ID)
        jenkins_hook._config['jenkins_hook_url'] = new_url
        jenkins_hook.edit(jenkins_hook._name, jenkins_hook._config)
        
        module_logger('Jenkins Hook Url Updated')