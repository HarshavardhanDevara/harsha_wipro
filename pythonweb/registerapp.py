# from flask import Flask,render_template, request
 
# #create a flask application
# app = Flask(__name__)
 
# @app.route('/')
# def home():
# 	return render_template('readdata.html');
 
 
# @app.route('/welcome/<name>')
# def greeting(name):
# 	return render_template('welcome.html',sname=name);
 
# @app.route('/person',methods=['POST'])
# def personData():
#    data = request.get_json()
#    name = data.get('name')
#    city = data.get('city')
#    pin = data.get('pin')
#    return render_template('data.html',sname=name,scity=city,spin=pin);
 
# @app.route('/register',methods=['POST'])
# def registerData():
#    name = request.form['name'];
#    city = request.form['city'];
#    pin = request.form['pin'];
#    return render_template('data.html',sname=name,scity=city,spin=pin);
 
 
# if __name__ == '__main__':
#    app.run(debug=True)


from flask import Flask, render_template, request

#create a flask application
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('readdata.html')

@app.route('/welcome/<name>')
def greeting(name):
    return render_template('welcome.html', sname=name)

@app.route('/person', methods=['POST'])
def personData():
   data = request.get_json()
   name = data.get('name')
   city = data.get('city')
   pin = data.get('pin')
   return render_template('data.html', sname=name, scity=city, spin=pin)

@app.route('/register', methods=['POST'])
def registerData():
   name = request.form['name']
   city = request.form['city']
   pin = request.form['pin']
   return render_template('data.html', sname=name, scity=city, spin=pin)

if __name__ == '__main__':
   app.run(debug=True)
