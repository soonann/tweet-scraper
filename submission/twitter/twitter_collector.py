'''

Name: TAN SOON ANN
Email: soonann.tan.2021@scis.smu.edu.sg

'''

from tweety import Twitter
from airflow.models import Variable
import json

def run_etl(**kwargs):
    
    username = Variable.get("username")
    password = Variable.get("password")
    topic_file = Variable.get("topic_file")
    output_dir = Variable.get("scrape_output_dir")
    pages = Variable.get("pages")

    # create a twitter session and login to twitter
    app = Twitter("session")
    app.sign_in(username, password)

    # read the topic file
    with open(topic_file, 'r') as topic_file:

        # iterate each topic and scrape for tweets
        for topic in topic_file:

            topic = topic.strip("\n")
            tweets = []
            print(f"topic {topic}: getting {topic} topic")

            # get the tweets related to the topic and append them to main list
            search_obj = app.search(topic, pages=pages, wait_time=2)
            for tweet in search_obj:
                print(tweet)
                tweets.append(tweet)

            # save all the tweets in main list to a json file named {topic}.json
            with open(f'{output_dir}/{topic}.json', 'w') as f:
                json.dump(
                    tweets,
                    f,
                    indent=4,
                    sort_keys=True,
                    default=str
                )

