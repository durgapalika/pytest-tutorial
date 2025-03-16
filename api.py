import requests


def get_posts(post_id: int):
    response = requests.get(f"http://jsonplaceholder.typicode.com/posts/{str(post_id)}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("something went wrong!!")

