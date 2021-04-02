import praw #python reddit API wrapper

print("\nWelcome to Reddit Climate Change Feed Looper : \n")

#create a reddit instance
#read only instance for extracting public info
#authorized instance for working as a normal reddit account
reddit = praw.Reddit(client_id = "my id", client_secret = "my secret", \
user_agent = "TheMarvellousThor")
#print(reddit.read_only)    read only instance

#create a subreddit instance i.e climatechange
subreddit = reddit.subreddit("climatechange")

#Access the submissions using various methods like top,hot,new,controversial,glided,rising etc
#they return a listing generator we need to iterate through
posts = list(subreddit.hot(limit = None))
print("NAME of Subreddit : ",subreddit.display_name)
print("Description :\n",subreddit.description)
print("")

i = 0
while i < len(posts):
    response = None
    while response != "Y" and response != "N":
        response = input("\nDo you want to see the next feed (Y)/(N) ? ").upper()
    if response == "N":
        print("Thank you..!")
        break
    print("-----------------------------------------------------------------------------------------------")
    print("\nTitle : ",posts[i].title)
    print("Upvotes : ",posts[i].score)
    if len(posts[i].selftext) > 1:
        print("Description :\n",posts[i].selftext+"\n")
    else:
        print("Description : NA\n")
    print("Author : ",posts[i].author)
    """
    for comment in post.comments:
        print(comment.body)
    """
    i -= 1
    print("-----------------------------------------------------------------------------------------------")              
    