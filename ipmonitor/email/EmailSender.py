'''
Created on Aug 12, 2013

@author: Christian
'''
import smtplib

class EmailSender:
    '''
    Sends an email using gmail as the SMTP server
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.props = self.__get_email_props__()

    def send_ip_change_notification(self, new_ip_address):
        '''
        Sends a notification indicating that the router's 
        External IP has changed
        '''
        username = self.props['username']
        sender = self.props['sender']
        password = self.props['password']
        recipient = self.props['recipient']
        server = self.props['smtp_server']
        port = self.props['smtp_port']
        
        subject = 'External IP Address has changed!'
        body = 'Your router\'s new external ip address is ' + new_ip_address
         
        headers = ["From: " + sender,
                   "Subject: " + subject,
                   "To: " + recipient,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
         
        session = smtplib.SMTP(server, port)
         
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(username, password)
         
        session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
        session.quit()

    def __get_email_props__(self):
        '''
        Returns a dictionary containing the email 
        recipient, username & password.
        
        Internal method. Do not use
        '''
        props = {}
        with open('email.properties') as f:
            for line in f:
                if line == '': continue
                val = line.strip().split("=")
                props[val[0]] = val[1]
                
        return props