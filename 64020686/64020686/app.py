from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def home():
	return render_template('index.html')
@app.route('/form/')

def form():
	return render_template('form.html')

@app.route('/register/')

def registerpage():
	return render_template('register.html')

if __name__ == '__main__':
  
	app.run(host='10.50.16.67',port=5000,debug=True)
