# This is the minimal import for a Flask app but there
# are numerous more important imports to make an actual
# app with multiple parts that will be introduced later.
from flask import Flask

# Just something you need to include up top:
app = Flask(__name__)

# To run this Flask app, activate your virtual environment
# and then type into terminal:
# $ python basic.py

# The Flask app will be hosted on a local server that you
# can navigate to on a browser through either:
# http://127.0.0.1:5000/     or     http://localhost:5000/
# Open up that page right now!


# The @app.route('/') line indicates what the URL
# extension will be. Since this route is labeled '/',
# it is refered to as the root, since it is the page
# you see when you navigate to 'http://localhost:5000/'

# The function name is arbitrary but I named it 'root'
# since it makes sense.

# If you changed the route to '/poop', then you'd need to go
# to 'http://localhost:5000/poop/' to see the 'Hello world!'.
# Try it! Comment out the current @app.route('/') line and
# uncomment the line below.

# You'll notice if you try to go to 'http://localhost:5000/'
# you'll get a Not Found error. You will only see the
# 'Hello world!' when you go to 'http://localhost:5000/poop/'

@app.route('/')
# @app.route('/poop')
def root():
    return 'Hello world!'

# This segment of code below is going to go at the end
# of every Flask app, along with the line at top that says:
# app = Flask(__name__)

# app.debug is set to True so that if the site bumps
# into an error, you will be redirected to a page with
# useful information about the error. In an actual launch
# of your website (i.e. on a server), you'd want to turn
# this to False or just not include it.
if __name__ == "__main__":
    app.debug = True
    app.run()

# After you finish exploring this simple app, go to the
# directory 'example_pages/' and read 'notes.txt' to start
# getting into something more functional.