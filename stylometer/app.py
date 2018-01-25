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

@app.route('/home')

@app.route('/text', methods=['POST'])
def textAnalyze():
	title = request.form["title"]
	text = request.form['textAreaItem']
	genre = request.form['Genre']
	vectorList, report = Submission(title, text, genre).genReport()
	session["vectorList"] = vectorList
	return render_template('report.html', report=report)

@app.route('/plot')
def dendroplot():

	vectorList = session.get("vectorList", None)
	img = dendroPlot(vectorList)
	png_data = base64.encodebytes(img.getvalue())
	'''
	img = BytesIO()
	y = [1,2,3,4,5]
	x = [0,2,1,3,4]

	plt.plot(x,y)
	plt.savefig(img, format='png')
	img.seek(0) # rewind to beginning of file
	png_data = base64.encodebytes(img.getvalue())
	'''
	session.clear() #TODO: make sure this placement doesn't cause bugs
	return render_template('dendroplot.html', png_data=png_data, vectorList=vectorList)


if __name__ == '__main__':    #initize web application
    app.run(debug=True)
