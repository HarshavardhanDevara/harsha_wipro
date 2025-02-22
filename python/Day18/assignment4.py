# Ass-4  Delete Post/2
# and makes sure it is deleted

import requests

url = "https://jsonplaceholder.typicode.com/posts/2"
delete_response = requests.delete(url)
if delete_response.status_code in [200, 204]:
    print("Post 2 deleted successfully!")
get_response = requests.get(url)

if get_response.status_code == 404:
    print("Post 2 is confirmed deleted!")
else:
    print("Post 2 still exists!")



