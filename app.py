from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def main():
	return show_requests();

@app.route('/requests')
def show_requests():
	res = requests.get('http://106.10.54.174/requests').json()
	if res['result'] != 'success':
		return render_template("error.html", error_msg=res['result'])
	return render_template("request_list.html", requests=res['requests'])

@app.route('/requests/<request_id>')
def show_request(request_id):
	res = requests.get('http://106.10.54.174/requests/' + request_id).json()
	if res['result'] != 'success':
		return render_template("error.html", error_msg=res['result'])
	return render_template("request_post.html", request_id=res['request']['request_id'], title=res['request']['title'], user_id=res['request']['user_id'], content=res['request']['content'])

@app.route('/delete_request/<request_id>')
def delete_request(request_id):
	res = requests.delete('http://106.10.54.174/requests/' + request_id).json()
	print(res)
	return show_requests()

@app.route('/notices')
def show_notices():
	res = requests.get('http://106.10.54.174/notices').json()
	if res['result'] != 'success':
		return render_template("error.html", error_msg=res['result'])
	return render_template("notice_list.html", notices=res['notices'])

@app.route('/notices/<notice_id>')
def show_notice(notice_id):
	res = requests.get('http://106.10.54.174/notices/' + notice_id).json()
	if res['result'] != 'success':
		return render_template("error.html", error_msg=res['result'])
	return render_template("notice_post.html", notice_id=res['notice']['notice_id'], title=res['notice']['title'], content=res['notice']['content'])

@app.route('/notice_form')
def register_notice():
	return render_template("notice_form.html")

@app.route('/create_notice', methods=['POST'])
def create_notice():
	notice = {'title': request.form['noticeTitle'], 'content': request.form['noticeContent']}
	res = requests.post('http://106.10.54.174/notices', notice).json()
	return show_notices()

@app.route('/delete_notice/<notice_id>')
def delete_notice(notice_id):
	res = requests.delete('http://106.10.54.174/notices/' + notice_id).json()
	print(res)
	return show_notices()

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8082, debug=True)
