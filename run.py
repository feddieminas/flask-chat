import os # access to enviroment variables
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET","randomstring123") #make secret key an enviromental variable
#app.secret_key = "randomstring123" # to generate a session id for cookie, we need to give to an app a secret_key
messages = []

def add_message(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S") # method takes a date/time object and converts it to a string on a given format
    messages.append({"timestamp": now, "from": username, "message":
        message})
    #messages.append("({}) {}: {}".format(now, username,message))

'''
def get_all_messages():
    """Get all of the messages and separate them with a 'br'"""
    return "<br>".join(messages)
'''

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    if "username" in session:
        return redirect(url_for("user", username=session["username"])) # ex redirect(session["username"]) - this will redirect to @app.route('/<username>') 
        # can use url_for to target the user view (def user(username) and username param
    
    return render_template("index.html")
    #return "To send a message use /USERNAME/MESSAGE" # want is to have it a s a URL www.flask/aaron/hello there
    #return "<h1>Hello There!</h1>"
    
@app.route('/chat/<username>', methods = ["GET", "POST"]) # better to insert chat and be more organised as having an about page
def user(username):
    """Add and display chat messages"""
    
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"])) # ex redirect(session["username"]) - this will redirect to @app.route('/<username>') 
    
    return render_template("chat.html", username=username, 
        chat_messages = messages)
    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    #return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())
    #return "Welcome, {0} - {1}".format(username, messages)
    #return "Hi " + username
    
'''    
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_message(username, message)
    return redirect(username) #redirect to the users personalized welcome page
    #return "{0}: {1}".format(username, message)
'''
    
app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=False) #we set ip and port values do not need to do later in Heroku




