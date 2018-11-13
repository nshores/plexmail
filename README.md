# PlexMail
Python tool to email and manage MyPlex shared users   
Inspiration and some code/logic taken from https://github.com/jakewaldron/PlexEmail/

**Differences between PlexMail and PlexEmail**
* PlexMail is written for Python 3.x
* PlexMail uses the [PlexApi](https://pypi.org/project/PlexAPI/) python library. This simplifies some of the needed requirments, and will make it more reliable when running
* PlexMail does not require installing any other libaries.
* PlexMail can be run from any machine, does not need to be local to plex.
* PlexMail can be run without a config, very useful for one-time notices, or integrating into another script. Simply specify `-u "myplexusername" and -p "myplexpassword` when running the script.
* PlexMail makes an attempt to expose all options with command line arguments.

**New Features**
* Ability to run without a configuration
* Ability to dump all user details to CSV 
* Dry run (See what's going to happen before sending emails)
* Send notice to one email only.

**Upcoming Features**
* Manage users (Add/Delete/Inivte)
* Email Templates





**Usage**

* Install Python 3.x
* Install PlexAPI (pip install plexapi)
* Clone repostiroy and run `main.py` with desired arguments

**Argument List**

TODO

**Edit the following variables in config.ini to fit your setup**

 	

~~~~
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
email_body = 'Nothing to see here yet'
#End SMTP Setup

 	

~~~~

Run with python3.x

    python3 main.py


