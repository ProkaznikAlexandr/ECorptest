from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

loged = False

@app.route("/", methods=['post','get'])
def login():
	
	if request.method == 'POST':
		global login, password
		login = request.form.get('login')
		password = request.form.get('password')


	if login == 'root' and password == 'toor':
		global loged
		loged = True
		return redirect(url_for('ip'))

	else:
		pass

	return render_template('login.html')

@app.route("/ip", methods=['post','get'])
def ip():
	return render_template('ip.html')

if __name__ == "__main__":
	app.run(debug=True)