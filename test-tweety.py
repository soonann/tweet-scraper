# twitte
from tweety import Twitter
import json

username = ""
password = ""
max = 30

# create a twitter session and login to twitter
app = Twitter("session")
app.sign_in(username, password)

# read the topic file
with open('topic.txt', 'r') as topic_file:

    # iterate each topic and scrape for tweets
    for topic in topic_file:

        topic = topic.strip("\n")
        tweets = []
        has_next = True
        print(f"topic {topic}: getting {topic} topic")

        # get the tweets related to the topic and append them to main list
        search_obj = app.search(topic, pages=10, wait_time=2)
        for tweet in search_obj:
            print(tweet)
            tweets.append(tweet)

        # save all the tweets in main list to a json file named {topic}.json
        with open(f'outputs/{topic}.json', 'w') as f:
            json.dump(
                tweets,
                f,
                indent=4,
                sort_keys=True,
                default=str
            )
