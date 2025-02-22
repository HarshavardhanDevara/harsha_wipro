import requests
url = 'https://www.skillsugar.com/examples/json/example_1.json'
 
result = requests.get(url)  # result is a variable of type response object
 
print("Encoding  =" , result.encoding) 	 #- the encoding that the document is using (UTF-8 .etc)
 
print("Headers   =" ,result.headers)   	 # - the response headers in JSON format
 
print("Cookies = " ,result.cookies)           # - the request cookies
 
print("Status Code =" ,result.status_code)       #- the status of the response in a code format (200, 500, 404 .etc.)
 
print("Content = " ,result.content)           #- the content of the response in binary format
 
print("Text  = " ,result.text )  #- the decoded content of the response according to the response encoding header  
                                 #  property
 
print("Redirect  =" ,result.is_redirect)       # - True if the response status code is a redirect, False if not
 
print("Time elaspsed =" ,result.elapsed)           #- the time between sending the request and getting a response
 
print("url  =" , result.url)               # - the URL of the request
 
print("Json  = " , result.json())            # - parse JSON content