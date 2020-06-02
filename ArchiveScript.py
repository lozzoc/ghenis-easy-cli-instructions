from piazza_api import Piazza
import json

CLASS_ID="k89brrt3pq17do"

with open("config.json", "r") as read_file:
    data = json.load(read_file)
    p = Piazza()
    print(data["user"])
    print(data["pass"])
    p.user_login()
    user_profile = p.get_user_profile()

    cs290 = p.network(CLASS_ID)
    posts = cs290.iter_all_posts(limit=50)
    for post in posts:
        print(post)
