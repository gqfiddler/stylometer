'''
launches responsive webpages using Flask
'''
from flask import Flask, render_template, request, session
from modules.submission import Submission
from modules.comparison.comparison import dendroPlot
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)
# set the secret key for sessions (disallows user from modifying cookies)
app.secret_key = 'B5Zy93g/3yQ T~XJK?jmM]EWP/!RO'

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/text', methods=['POST'])
def textAnalyze():
	session.clear()
	title = request.form["title"]
	text = request.form['textAreaItem']
	genre = request.form['Genre']
	vectorList, report = Submission(title, text, genre).genReport()
	img = dendroPlot(vectorList)
	png_data = base64.encodebytes(img.getvalue())
	return render_template('report.html', png_data=png_data, report=report)

if __name__ == '__main__':    #initize web application
    app.run(debug=True)
