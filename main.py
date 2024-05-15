from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
from instagrapi import Client

app = Flask(__name__)
app.secret_key = "LithiumIonBattery12!"
app.permanent_session_lifetime = timedelta(days=5)

global current_id
current_id = []

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user, password = request.form["nm"], request.form["pw"]
        session["user"], session["password"] = user, password
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    #print(current_id)
    if current_id == []:
        #if request.method == "POST":
            #current_id.append(request.form)
        if "user" in session:
            user = session["user"]
            password = session["password"]
            session["account_username"] = user
            session["account_password"] = password

            cl = login(user, password) #logs into accountW
            thread_dict = get_threads(cl)
            cl.logout()
            ids = []
            profile = []
            for info in thread_dict:
                ids += [info]
                profile += [thread_dict[info]]
            if request.method == "POST":
                #print(request.form["new_id"])
                current_id.append(request.form["new_id"])
                return redirect(url_for("user"))
            return render_template("user.html", thread_ids = ids, profile_info = profile, length = len(ids), current_id = current_id)
        else:
            return redirect(url_for("login"))
        
    elif current_id != []:
        #print(current_id, "<----------------------------")
        return redirect(url_for("messages"))

def login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD):
    cl = Client()
    cl.inject_sessionid_to_public()
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
    return cl

def get_threads(cl):#pfp, name, last_message, thread_id
    threads = cl.direct_threads()
    thread_dict = {} #dictionary to hold thread data as it is currently just attributes
    for thread in threads:
        temp = [] #temp list for profile data
        for info in thread.__dict__["users"][0].__dict__:
            temp += [thread.__dict__["users"][0].__dict__[info]] #adds each attribute to a list
        thread_dict[thread.__dict__["id"]] =  temp #forms the dictionary 
    return thread_dict


@app.route("/logout")
def logout():
    global current_id
    current_id = []
    session.pop("user", None)
    session.pop("password", None)
    return redirect(url_for("login"))

@app.route("/messages")
def messages():
    cl = Client()
    cl = login(session["account_username"], session["account_password"])
    global current_id
    id = current_id[0][:]
    all_messages = get_all_messages(cl, id)
    print(all_messages)
    return render_template("messages.html", thread_id = id, messages = all_messages, length = len(all_messages))

def get_all_messages(cl, thread_id):
    messages = cl.direct_messages(thread_id = thread_id)
    message_details = []
    for message in messages:
        #print(type(message))
        #print(message.__dict__)
        temp = []
        for item in message.__dict__:
            if item not in ["id", "user_id", "thread_id", "is_shh_mode", 'reel_share', 'story_share', 'animated_media','media_share','felix_share','xma_share','clip','placeholder']:
                if item == "type" and message.__dict__[item] not in ["text"]:
                    pass
                else:
                    temp.append(message.__dict__[item])
        if temp[1] == "text":
            message_details.append(temp)
    return message_details


if __name__ == "__main__":
    app.run(debug=True)
'''
plan:
take user name and password
use the login creds to link to the insta api
display data
'''