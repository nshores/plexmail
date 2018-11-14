#!/usr/bin/python3
#Requires python-plexapi
#https://github.com/pkkid/python-plexapi
#'pip install plexapi'

from plexapi.myplex import MyPlexAccount
from mail_send import send_mail
import configparser
import sys
import argparse
import logging
import plexapi
import os.path

parser = argparse.ArgumentParser(description='This script emails your plex users')
parser.add_argument('--whatif', help='Do a dry run of the script, dont send anything ', action='store_true')
parser.add_argument('-n','--notice', help='Notice Mode -- Send 1 time notice (Text passed here will go in email)')
parser.add_argument('-u','--username', help='MyPlex Username')
parser.add_argument('-p','--password', help='MyPlex Password')
parser.add_argument('--smtp_server', help='SMTP Server')
parser.add_argument('--smtp_username', help='SMTP Username')
parser.add_argument('--smtp_password', help='SMTP Password')
parser.add_argument('--smtp_port', help='SMTP Port')
parser.add_argument('--smtp_send_as', help='SMTP Send-As User')
parser.add_argument('-t','--target_user', help='Email one specific user')
parser.add_argument('-d','--dump', help='Dump All User information to file')
parser.add_argument('-c','--config', help='Custom Config File')
parser.add_argument('--disable_email', help='Set to disable sending emails', default=False, action='store_true')
args = parser.parse_args()

#Dry run flag
WhatIf = False
if args.whatif == True:
     WhatIf = True
     print('---Dry Run Enabled---- ')

#Email flag

if args.disable_email == False:
     disable_email = False
     print('---Email Sending Enabled---- \n')
else:
    disable_email = True

# Load custom config
if args.config:
    config_location = args.config
    print("Loading custom configuration")
    config = configparser.ConfigParser()
    config.read(config_location)
    plex_username = config['plex']['plex_username']
    plex_password = config['plex']['plex_password']
    email_username = config['email']['email_username']
    email_password = config['email']['email_password']
    email_host = config['email']['email_host']
    email_from = config['email']['email_from']
    email_port = config['email']['email_port']
    email_body = config['email']['email_body']
    email_subject = config['email']['email_subject']

#try to load default config
elif os.path.isfile('config.ini'):
    print("Found local configuration file\n")
    config = configparser.ConfigParser()
    config.read('config.ini')
    plex_username = config['plex']['plex_username']
    plex_password = config['plex']['plex_password']
    email_username = config['email']['email_username']
    email_password = config['email']['email_password']
    email_host = config['email']['email_host']
    email_from = config['email']['email_from']
    email_port = config['email']['email_port']
    email_body = config['email']['email_body']
    email_subject = config['email']['email_subject']

else:
    #Parse command line configuration options
    print("No configuration found -- using command line arguments\n")
    #Replace regular email body from template with a parmater
    if args.notice:
        email_body = args.notice
    if args.username:
        plex_username = args.username
    if args.password:
        plex_password = args.password
    if args.smtp_username:
        email_username = args.smtp_username
    if args.smtp_password:
        email_password = args.smtp_password
    if args.smtp_server:
        email_host = args.smtp_server
    if args.smtp_port:
        email_port = args.smtp_port
    if args.smtp_send_as:
        email_from = args.smtp_send_as


#create 'MyPlexAccount' PlexAPI Object
print("Logging into MyPlex\n")
try:
    plex = MyPlexAccount(plex_username, plex_password)
    print("...Success\n")
except plexapi.exceptions.BadRequest as err:
    print("MyPlex Login Error: {0}\n".format(err))
    print("Stopping Script")    
    sys.exit()


#Define Some helper functions 

#Let's grab a server name. Returns LAST match if multiple servers are found.. Fix me at some point..
def plex_server_name():
    resource = plex.resources()
    Plex_Server_Name = ""
    for r in resource:
        if r.product == 'Plex Media Server' and r.owned == True:
            Plex_Server_Name = r.name
    return Plex_Server_Name

    

def plex_email_list():
    #Grab a list of user objects
    userlist = plex.users()
    #create list for email
    emaillist = []
    for user in userlist:
        #add to list
        emaillist.append(user.email)
    return emaillist

#EMAIL CREATION SECTION
#Check to see if email is disabled with a flag
if disable_email == False:
    #Send email flag is set, let's create an email
    
    #Subject Line
    #Scan for a custom subject line in the config. It doesn't exist, let's make a nice default by grabbing the local plex server name.
    if not email_subject:
        email_subject = 'Notification From {}'.format(plex_server_name())
    #Body Section
    #TODO

#END EMAIL CREATION SECTION

#Main program logic
def main():
    #call function to grab list of user emails
    user_email_list = plex_email_list()

    #Decide what to do
    if disable_email == False:
        #Send some emails
        for user in user_email_list:
            send_to_address = user
            if WhatIf == True:
                print(f"Sending email to {send_to_address} --DRY RUN NOT SENDING EMAIL--")
            else:
                print(f"Sending email to {send_to_address}")
                send_mail(
                email_host, 
                email_port, 
                email_username, 
                email_password, 
                send_to_address, 
                email_body, 
                email_subject) 
    else:
        print("Nothing to do!")

if __name__ == '__main__':
    main()