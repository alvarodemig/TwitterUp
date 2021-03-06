import time, tweepy

#Authenticating the access
CONSUMER_KEY = 'AppConsumerKey'
CONSUMER_SECRET = 'AppConsumerSecret'
ACCESS_KEY = 'UserAccessKey'
ACCESS_SECRET = 'UserAccessSecret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Obtaining your friends (following) list
friends_list = api.friends_ids('yourtwitteraccount')

#Unfollowing
for friend in friends_list:
    try:
        api.destroy_friendship(friend)
        print 'Unfollowed user ' + str(friend)
    except:
            print '---- UNFOLLOWING FAILED ---'
    #You can include a waiting time (seconds) between each unfollowing
    time.sleep(1)
