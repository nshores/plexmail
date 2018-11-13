#!/usr/bin/python3
#https://github.com/pkkid/python-plexapi
import plexapi
import smtplib

plex_username = 'theslimone'
plex_password = 'nickisawesome420'
email_username = 'nick@shoresmedia.com'
email_password = 'Jo5R58KOKtRV'


#create 'MyPlexAccount' PlexAPI Object
plex = plexapi.myplex.MyPlexAccount(plex_username, plex_password)

def plex_email_list():
    #Grab a list of users
    userlist = plex.users()

    #create list for email
    emaillist = []
    for user in userlist:
        #add to list
        emaillist.append(user.email)
    return emaillist


s = smtplib.SMTP(host='smtp.office365.com', port=587)
s.starttls()
s.login(email_username, email_password)

