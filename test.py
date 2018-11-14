email_subject = 'test'
#Main program logic
def main():
    #call function to grab list of user emails
    user_email_list = plex_email_list()

    #Put together an email
    if email_subject == None:
        email_subject = 'Notification From {}'.format(plex_server_name())

    #Send some emails
    for user in user_email_list:
        send_to_address = user
        if WhatIf == True:
            print(f"Sending email to {send_to_address} --DRY RUN NOT SENDING EMAIL--")
        else:
            print(f"Sending email to {send_to_address}")
            send_mail(email_host, email_port, email_username, email_password, send_to_address, email_body, email_subject) 
        

if __name__ == '__main__':
    main()