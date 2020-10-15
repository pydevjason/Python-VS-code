import praw

reddit = praw.Reddit(client_id = "rYxVSShoqrOyUQ",
					client_secret = "3smx9K5ob-_bMgdqHW8dmoDoFp0",
					username = "username",
					password = "password",
					user_agent = "anything",
					)

subreddit = reddit.subreddit("python")

top_python = subreddit.top(limit = 5)
hot_python = subreddit.hot(limit = 5)

for i in top_python:
	if not i.stickied:
		print()
		print(f"Title: {i.title},\n Ups: {i.ups}, Downs: {i.downs}, Have we visited: {i.visited}, Score: {i.score}, url: {i.url}")

print()

for submission in hot_python:
	print(submission.author)

subreddit.subscribe()

# for j in hot_python:
# 	print(j.comments)

# other things you can do to take action:
# .upvote()
# .downvote()
# .reply()

