from dotenv import dotenv_values
import os
from pymongo import MongoClient
from tqdm import tqdm

config = dotenv_values(dotenv_path=os.path.join("db-service", ".env"))

client = MongoClient(config["ATLAS_URI"])


def add_media_to_posts():
    post_collection = client["annotator"]["posts"]
    source_collection = client["aggregator"]["sources"]

    for post in tqdm(
        post_collection.find(),
        desc="Adding media to posts",
        total=post_collection.count_documents(filter={}),
    ):
        source_ids = post["source_ids"]

        for source_id in source_ids:
            if (source := source_collection.find_one({"_id": source_id})) is not None:
                media = source["media"]
                post_collection.update_one(
                    {"_id": post["_id"]}, {"$set": {"media": media}}
                )
                break


if __name__ == "__main__":
    add_media_to_posts()
