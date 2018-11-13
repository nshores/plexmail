#!/usr/bin/python3
#Requires python-plexapi
#https://github.com/pkkid/python-plexapi
#'pip install plexapi'

from plexapi.myplex import MyPlexAccount
from mail_send import send_mail

#Plex Setup
plex_username = 'xxxx'
plex_password = 'xxxxx'
#End Plex Setup

#SMTP Setup
email_username = 'xxxx'
email_password = 'xxxxx'
email_host = 'smtp.office365.com'
email_from = 'xxxx'
email_port = '587'
#TODO - Replace with template
email_body = 'Nothing to see here yet'
#End SMTP Setup


#create 'MyPlexAccount' PlexAPI Object
plex = MyPlexAccount(plex_username, plex_password)

def plex_email_list():
    #Grab a list of users
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
        print(f"Sending email to {send_to_address}")
        #send_mail(email_host, email_port, email_username, email_password, send_to_address, email_body) 

if __name__ == '__main__':
    main()




