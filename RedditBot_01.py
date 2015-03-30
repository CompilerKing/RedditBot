import praw
import time

# FUTURE IMPROVEMENTS: create bot that looks for x-post titles
#                       posts comment linking to the subreddit
#                       x-posted to in the title
#                       reads log in info from file instead of typing each time

r = praw.Reddit(user_agent = "RedditBot by Samuel Decanio --- Type T.B.D.")
r.login()
print("Logging in....")

words_to_watch = ['definately', 'defiantly', 'definatly', 'definetly', 'definatley']
cache = []

def run_bot():
    print("Grabbing the subreddit....")
    # the subreddit it searches.... all = /r/all
    subReddit = r.get_subreddit("test")
    print("Acquiring comments...")
    comments = subReddit.get_comments(limit = 25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_watch)
        if comment.id not in cache and isMatch:
            print("Match found! Comment ID: " + comment.id)
            comment.reply("I believe you meant definitely.")
            cache.append(comment.id)
            print("Replied successfully")

    print("Loop finished... Taking a breather...")

while True:
    run_bot()
    time.sleep(10)