from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import time
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/samay'
db = SQLAlchemy(app)

class Contact(db.Model):
    
    email = db.Column(db.String(120),  primary_key=True)
    phone = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=False)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contact(email=email, phone=phone, message=message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


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

@app.route('/contact_page')
def contact_page():
    return render_template('contact.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

if __name__ == '__main__':
    app.run(debug=True)
