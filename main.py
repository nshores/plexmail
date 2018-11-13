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
parser.add_argument('--smpt_port', help='SMTP Port')
parser.add_argument('--smtp_send_as', help='SMTP Send-As User')
parser.add_argument('-t','--target_user', help='Email one specific user')
parser.add_argument('-d','--dump', help='Dump All User information to file')
args = parser.parse_args()

#Dry run flag
WhatIf = False

if args.whatif == True:
     WhatIf = True
     print('---Dry Run Enabled---- \n')

# Load the configuration file
if os.path.isfile('config.ini'):
    print("Found local configuration file\n")
    config = configparser.ConfigParser()
    config.read('config.ini')
    #CONFIG
    plex_username = config['plex']['plex_username']
    plex_password = config['plex']['plex_password']
    email_username = config['email']['email_username']
    email_password = config['email']['email_password']
    email_host = config['email']['email_host']
    email_from = config['email']['email_from']
    email_port = config['email']['email_port']
    email_body = config['email']['email_body']
    #CONFIG
else:
    print("No configuration found -- using command line arguments\n")
    #Replace regular email body from template with a parmater
    if args.notice:
        config['email']['email_body'] = args.notice



#create 'MyPlexAccount' PlexAPI Object
print("Logging into MyPlex\n")
try:
    plex = MyPlexAccount(plex_username, plex_password)
except plexapi.exceptions.BadRequest as err:
    print("MyPlex Login Error: {0}\n".format(err))
    print("Stopping Script")

    sys.exit()

def plex_email_list():
    #Grab a list of user objects
    userlist = plex.users()

    #create list for email
    emaillist = []
    for user in userlist:
        #add to list
        emaillist.append(user.email)
    return emaillist

def main():
    user_email_list = plex_email_list()
    for user in user_email_list:
        send_to_address = user
        if WhatIf == True:
            print(f"Sending email to {send_to_address} --DRY RUN NOT SENDING EMAIL--")
        else:
            print(f"Sending email to {send_to_address}")
            #send_mail(email_host, email_port, email_username, email_password, send_to_address, email_body) 
        

if __name__ == '__main__':
    main()