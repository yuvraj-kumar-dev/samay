from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/')
def index():
    userTime = time.strftime('%H:%M:%S')
    return render_template('index.html', userTime=userTime)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)
