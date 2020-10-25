from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('homepage.html')

@app.route('/anotherpage')
def chicken():
    return render_template('anotherpage.html')

if __name__ == "__main__":
    app.debug = True
    app.run()