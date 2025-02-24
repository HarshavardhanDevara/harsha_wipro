from http.cookies import SimpleCookie
from http.cookies import SimpleCookie
# Create a cookie
cookie = SimpleCookie()
cookie["username"] = "harsha"
cookie["username"]["path"] = "/"  # Set path
cookie["username"]["max-age"] = 3600  # Expiry time in seconds
 
# Convert to HTTP header format

cookie_header = cookie.output(header="")  

print(cookie_header)  # Set-Cookie: username=JohnDoe; Path=/; Max-Age=3600

 