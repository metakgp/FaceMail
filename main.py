import facebook
import json
import email_functions
post_id = json.load(open('post_id.json' , 'r'))   #reading json file containing last post ids

last_fb_post_data = facebook.reading_last_post()  #reading facebook post
if last_fb_post_data['id'] != post_id['last_fb_post_id'] and last_fb_post_data['id'] != post_id['last_post_by_email_id'] :
    post_id['last_fb_post_id'] = last_fb_post_data['id']   #changing the last post id
    email_functions.send_mail("New Post on MetaKGP facebook page" , last_fb_post_data['message'])


#reading mail
email_dict = email_functions.reading_mail()  #getting all the mail arguments
if email_dict['subject'].lower() == "post" :
    id  = facebook.publishing_post(email_dict['msg_body'])
    if id != 0 :
        post_id['last_post_by_email_id'] = id
    else :
        print ("There was some error while posting")
post_id = json.dumps(post_id)
file_obj = open('post_id.json' , 'w')
file_obj.write(post_id)
file_obj.close()



