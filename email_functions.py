'''
reading_mail() - takes no input and returns a dictonary with mail argumnets as dict['subject']  , dict['msg_body']
send_mail() - takes 2 arguments - subject , message and returns 1 if message is sent successfully and 0 is a error occurs
'''
import gmail
import smtplib
import json
from email.mime.text import MIMEText
import Logger
logger = Logger.Logger(name='RunLog')
credentials = json.load(open('CONFIG', 'r'))
def reading_mail () :  # this function returns a dictionary with email arguments
	g = gmail.Gmail()
	g.login(credentials['email'], credentials['pass'])  #logging in to gmail server
	unread = g.inbox().mail(unread=True)  #getting all unread mails. It returns all the blank mials
	unread[-1].fetch()   # getting all the mail attributes like body,subject etc
	mail_args = {'subject' : unread[-1].subject , 'msg_body' : unread[-1].body}
	unread[-1].read()  #marking the mail as read
	return mail_args
	g.logout()  #logging out
def send_mail(mail_subject,mail_body) :
	credentials = json.load(open('CONFIG', 'r'))
	msg = MIMEText(mail_body)
	msg['Subject'] = mail_subject
	#sending mail
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(credentials['email'],credentials['pass'])
		server.sendmail(credentials['email'], credentials['to'], msg.as_string())
		server.quit()
		return True
	except :
		return False
	