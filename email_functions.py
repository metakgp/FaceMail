'''
reading_mail() - takes no input and returns a dictonary with mail argumnets as dict['subject']  , dict['msg_body']
send_mail() - takes 2 arguments - subject , message and returns 1 if message is sent successfully and 0 is a error occurs

'''

from gmail import Gmail
import smtplib
import json
from email.mime.text import MIMEText
credentials = json.load(open('credentials.json', 'r'))
def reading_mail () :  # this function returns a dictionary with email arguments
    g = Gmail()
    g.login(credentials['from_email'], credentials['from_pass'])  #logging in to gmail server
    unread = g.inbox().mail(unread=True)  #getting all unread mails. It returns all the blank mials
    unread[-1].fetch()   # getting all the mail attributes like body,subject etc
    mail_args = {'subject' : unread[-1].subject , 'msg_body' : unread[-1].body}
    unread[-1].read()  #marking the mail as read
    return mail_args
    g.logout()  #logging out
def send_mail(mail_subject , mail_body) :
    msg = MIMEText(mail_body)
    msg['Subject'] = mail_subject
    #sending mail
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(credentials['from_email'],credentials['from_pass'])
        server.sendmail(credentials['from_email'], credentials['to_email'], msg.as_string())
    except :
        print "Error: unable to send email"
    server.quit()
