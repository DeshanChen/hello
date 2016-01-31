from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello():
"""	return render_template ('te.html')
"""
        return 'hello world'
if __name__ == '__main__':
	app.run('0.0.0.0', debug=True)

	
