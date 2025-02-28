from flask import Flask
 
 
#create a flask application
app = Flask(__name__)
 
#Define route for the requests
@app.route('/') 
def home1():
  return "Hello, Welcome to Flask - Home Page- Get Mapping";
 
#Define route for the requests
@app.route('/test1/<name>/<city>') 
def home3(name,city):
  return "Hello, "+name+" Welcome to "+city;
 
 
@app.route('/post', methods=['POST']) 
def home2():
  return "Hello, Welcome to Flask - Home Page- POST Mapping";
 
 
@app.route('/put', methods=['PUT'])
def test1():
  return "PUT method is called....";
 
@app.route('/del', methods=['DELETE'])
def test2():
  return "Delete method is called....";
 
 
if __name__ == '__main__':
   app.run(debug=True)