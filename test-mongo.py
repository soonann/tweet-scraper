import json
import os
from pymongo import MongoClient, errors

# output dir of the scraped tweets
dir = 'outputs'

# for each file in the dir
for topic_filename in os.listdir(dir):
    succ = 0
    fail = 0

    # if the file sub item is a json file
    topic_filepath = os.path.join(dir, topic_filename)
    if os.path.isfile(topic_filepath) and ".json" in topic_filepath:

        # load the json file as an object
        with open(topic_filepath, 'r') as f:
            topics = json.load(f)
            topic_name = topic_filename[:-5]

            # connect to mongo
            client = MongoClient('mongodb://mongo:mongo@localhost:27017/')
            db = client['twitter']
            collection = db[topic_name]
            collection.create_index([("tweet_id", 1)], unique=True)
            for tweet in topics:
                # check if there is a valid id and text field
                if tweet["id"] and tweet["text"]:
                    doc = {
                        "tweet_id": tweet["id"],
                        "tweet_text": tweet["text"]
                    }

                    # handle duplicate key errors
                    try:
                        result = collection.insert_one(doc)
                    except errors.DuplicateKeyError:
                        fail += 1
                        continue

                    # Check if the operation was successful
                    if result.acknowledged:
                        succ += 1
                    else:
                        fail += 1

    print(f"topic: {topic_name}, total successful inserts: {succ}")
    print(f"topic: {topic_name}, total failed inserts: {fail}")

    # delete the file
    try:
        os.remove(topic_filepath)
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}")
