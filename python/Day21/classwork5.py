import logging

import requests
 
# Configure logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
def log_http_request(url):

    logging.info(f"Sending request to {url}")

    response = requests.get(url)

    logging.info(f"Response Status Code: {response.status_code}")

    logging.info(f"Response Body: {response.text[:200]}")  # Log first 200 characters
 
    return response
 
# Example usage

log_http_request("https://jsonplaceholder.typicode.com/posts/1")

 
# logging http Requests
 