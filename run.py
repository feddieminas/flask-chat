import os # access to enviroment variables
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE" # want is to have it a s a URL www.flask/aaron/hello there
    #return "<h1>Hello There!</h1>"
    
@app.route('/<username>') 
def user(username):
    return "Hi " + username
    
@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True) 




