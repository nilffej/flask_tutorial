# HELLO! START HERE!

# Here we have some new imports that will be essential in building
# an app from an HTML page and multi-page apps.

# render_template() renders an HTML page from the directory 'templates/'.
# redirect() redirects you to a specific URL.
# url_for() is a URL builder.

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# Run this file with
# $ python app.py
# and as you navigate through the website, follow the code
# code to see how all the parts function together.

# ----- STEP 1 -----
# Go to http://localhost:5000/
# Here you're rendering 'homepage.html'.
# render_template() takes in a filename, as well as optional
# parameters defined by the user that can be used as variables
# in the HTML file. Here, I've passed in a variable random_text
# with a string that says 'Hey there!'.
# This is the root page. Go checkout the 'homepage.html' file.
@app.route('/')
def root():
    return render_template('homepage.html',
        random_text='Hello there!')



# ----- STEP 3 -----
# This function comes into play when you click
# Click Here! on the root page.
# Here you're rendering 'anotherpage.html'.
# Go check out the 'anotherpage.html', read the top
# text about Jinja, and then find STEP 4.
@app.route('/nothomepage')
def chicken():
    return render_template('anotherpage.html')



# Here you're using redirect() to redirect to a URL
# generated by url_for(). url_for() will generate the URL
# associated with root() by using the @app.route('/').
# Hence, you will be redirected to 'http://localhost:5000/'.
# Notice you'll never really see the page 
# 'http://localhost:5000/alternateroute'. This page
# doesn't really exist; this function is just a pathway to root.
@app.route('/alternateroute')
def beef():
    return redirect(url_for('root'))


# Here you're redirecting the page to Google's
# homepage using redirect().
@app.route('/gotogoogle')
def go_to_google():
    return redirect('https://www.google.com/')



if __name__ == "__main__":
    app.debug = True
    app.run()