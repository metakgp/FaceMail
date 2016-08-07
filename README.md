# FaceMail
This script sends email when a new post is posted on the Facebook page and also can post the body of the message via facebook page.

Create two JSON files in the root directory as follows  : 
1. credentials.json
{
	"from_email" : "senders_email" , 
	"from_pass" : "senders_password",
	"to_email" : "receivers_email" ,
	"fb_page_id" : "id of the facebook page to look " ,
  "token": "Access Token"
}

2. post_id.json (just copy the below the code for this file)
   {"last_fb_post_id": "id",  "last_post_by_email_id": "id"}


Modules Required : facepy , pygmail
   
   
