from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the homepage!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'Contact us at example@example.com.'

if __name__ == '__main__':
    app.run()
