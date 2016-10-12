#import facebook
import json
import email_functions
try :
	post_id = json.load(open('post_id.json' , 'r'))   #reading json file containing last post ids
	flag = False  
except :
	post_id = {"last_fb_post_id": "id", "last_post_by_email_id": "id"}
	flag = True
metakgp_data = json.load(open('metakgp.json','r'))  #open the json data file 
mail_msg = ""
post_no = 1
for item in metakgp_data :
	print item['id']
	if (item['id'] == post_id['last_fb_post_id']) or (item['id'] == post_id['last_post_by_email_id']) :
		break 
	else : 
		mail_msg += "Post No. {}\n{}\n\nPosted On : {} at {}\nLink to the post : https://www.facebook.com/{}\n\n".format(str(post_no),item['message'],item['real_date'],item['real_time'],item['id'] )
		post_no += 1
	if post_no == 2 and flag :
		break
if mail_msg is not "" :
	print "Sending mail"
	email_functions.send_mail("New Post on MetaKGP facebook page" , mail_msg)
	post_id['last_fb_post_id'] = metakgp_data[0]['id']
else :
	print "No new post"
#reading mail
# email_dict = email_functions.reading_mail()  #getting all the mail arguments
# if email_dict['subject'].lower() == "post" :
#     id  = facebook.publishing_post(email_dict['msg_body'])
#     if id != 0 :
#         post_id['last_post_by_email_id'] = id
#     else :
#         print ("There was some error while posting")
#print post_id
json.dump(post_id,open('post_id.json' , 'w'))



