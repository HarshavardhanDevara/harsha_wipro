from http.cookies import SimpleCookie
 
# Create a cookie
cookie = SimpleCookie()
cookie["username"] = "harsha"
cookie["Age"]= "25"  
cookie["username"]["max-age"] = 120  # Expiry time in seconds
 
# Convert to HTTP header format
cookie_header = cookie.output(header="")  
print(cookie_header)  
 