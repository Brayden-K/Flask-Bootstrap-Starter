from flask import Flask, url_for, render_template
#Load sql handler
from utilities.sql import SQL

#Initialize flask
app = Flask(__name__)

#Debug allows us to auto-reload when you save.
app.debug = True

#Context_processor allows you to set global variables.
@app.context_processor
def inject_settings():
    MySQL = SQL()
    settings = {"settings": MySQL.Settings()}
    return settings

#Our index route
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()