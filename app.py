from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("login.html")

@app.route('/requests')
def show_requests():
	res = requests.get('http://106.10.54.174/requests').json()
	if res['result'] != 'success':
		return render_template("error.html", err=res['result'])
	return render_template("request_list.html", requests=res['requests'])

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8082, debug=True)
