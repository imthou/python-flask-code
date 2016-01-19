import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    author = "Tim's"
    name = "Liz"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods= ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)