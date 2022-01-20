import tweepy
# the Tweepy module is what allows us to use the twitter API functionalities through Python

#import time
# the time module allows us to let the program take a break in case it's overloading. We usually don't have to use it unless we have this code running automatically.

consumer_key = 'KCZ7xPYozByQbpu3s026RBWvt'
consumer_secret = 'O0kl1kknzRb23cdyR3CJx4shouuGgTqGY8fGRQ0LpKAmPG6jSg'
key = '1435051901607833603-dloV1Nq6fBtiQMZus3OleahXg91amJ'
secret = 'repY71RZVkKYrA0Ci8c3atqA4YY4JJxsOvIKqseNjFU86'

# we create variable corresponding to the generated keys and tokens 

tweepy.OAuthHandler

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
# this code uses functions from the Tweepy module to authenticate the API account using the generated keys and tokens

user = api.me() # this gives us access to every piece of information regarding this bot account
print(user.screen_name) # For example we can use it to print the account's username


# 1/ we will now try to write a tweet

def tweeting():
    tweet = input('Type a Tweet: ')
    # this input allows the user to write a tweet
    api.update_status(tweet)
    # the update status function allows the user to tweet

# in order to use this function: run the function then input the content of the tweet that you wish to post.    

# 2/ we will now try to reply to tweets that mention the bot
idfile = "lastTweetId.txt"

def readId(file_name):
    filetoread = open(file_name, 'r')
    last_seen_id = int(filetoread.read())
    filetoread.close()
    return last_seen_id

def storeId(file_name, last_seen_id):
    filetowrite = open(file_name, 'w')
    filetowrite.write(str(last_seen_id))
    filetowrite.close()
    return
# these functions are for reading then storing the ID of the last tweet the bot replies to

def replying(): 
    your_reply = input('Your reply: ')

    myTimeline = api.mentions_timeline(readId(idfile)) # this allows us to access the tweets in our timeline starting from the last tweet we replied to 

    for atweet in reversed(myTimeline): # we reverse the timeline list in order to access the latest tweets and not the oldest
        print(str(atweet.id) + ": " + atweet.text)
        api.update_status('@'+ atweet.user.screen_name + ' ' + your_reply)
        storeId(idfile, atweet.id) #storing the ID of the last tweet we replied to 

# In order to use this function: Mention the bot from another twitter account, then run this function and input what you wish for the bot to reply


# 3/ we will now try to retweet and like tweets containing a specific key word
def retweetandlike():
    search = input("search a term: ")
    numberOfTweets = int(input("how many tweets: "))
    # these inputs demand the search term and the number of tweets we want to go through
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        tweet.retweet()
        tweet.favorite()
        print("liked and retweeted")

# in order to use this function: run the function and then input a keyword and the number of tweets containing the keyword that you want to retweet and like. If there aren't enought tweets containing the keyword the function will present an error because it can't retweet and like the same tweet twice.
        
        
# 4/ we will now try to tweet images
def uploadImage():
    thetweet = input("your caption: ")
    image = input("image name: ")
    api.update_with_media(image,thetweet)

# in order to use this function: put an image file in the folder containing the code for the bot and call this function. The function will simply ask the user to input the caption and the name of the image file (for example: waves.jpg)

user_name = 'kfrworks'
api.create_friendship(user_name)

#tweeting()
#replying()
#retweetandlike()
#uploadImage()