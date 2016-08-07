'''
reading_last_posts() : takes no input and returns a dictonary of post data like ['id'] , ['message']
publishing_post()  : takes one argument which is the message to post returns id of the published post or 0 is there is any error

'''


from facepy import GraphAPI
import facepy
import json
credentials = json.load(open('credentials.json', 'r'))
try :
    graph = GraphAPI(credentials['token'])
except Exception, e:
    print e
def reading_last_post() :
    x = graph.get('me/posts')
    return x['data'][0]  # printing latest post
def publishing_post(msg) :
    try :
        post_id = graph.post("%s/feed?message=%s" % ( credentials['fb_page_id'] ,msg ) )  #posting on the page and getting the post's id
        print "publish success"
        return post_id['id']
    except Exception, e:
        print e
        return 0