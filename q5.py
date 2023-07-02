import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def get_posts():
    response = requests.get(BASE_URL)
    return response.json()


def get_posts_by_id(post_id):
    url = f"{BASE_URL}/{post_id}"
    response = requests.get(url)
    return response.json()


def create_post(title, author):
    data = {"title": title, "author": author}
    response = requests.post(BASE_URL, json=data)
    return response.json()


def update_post(post_id, title, author):
    url = f"{BASE_URL}/{post_id}"
    data = {"title": title, "author": author}
    response = requests.put(url, json=data)
    return response.json()


def delete_post(post_id):
    url = f"{BASE_URL}/{post_id}"
    response = requests.delete(url)
    return response.json()


def main():
    # GET
    posts = get_posts()
    print("GET All posts:")
    print(posts)

    # GET BY ID
    post_id = 1
    post = get_posts_by_id(post_id)
    print("\nGET post by ID:")
    print(post)

    # POST
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    new_post = create_post(title, author)
    print("\nPOST (Create) post:")
    print(new_post)

    # PUT
    post_id = 1
    updated_title = "New Title"
    updated_author = "New Author"
    updated_post = update_post(post_id, updated_title, updated_author)
    print("\nPUT (Update) post:")
    print(updated_post)

    # DELETE
    post_id = 1
    deleted_post = delete_post(post_id)
    print("\nDELETE post:")
    print(deleted_post)


if __name__ == "__main__":
    main()
