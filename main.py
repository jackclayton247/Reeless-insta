from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta
from instagrapi import Client

app = Flask(__name__)
app.secret_key = "yoyo"
app.permanent_session_lifetime = timedelta(minutes=5)

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

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        password = session["password"]
        cl = login(user, password) #logs into account
        thread_dict = get_threads(cl)
        ids = []
        profile = []
        for info in thread_dict:
            ids += [info]
            profile += [thread_dict[info]]
        return render_template("user.html", thread_ids = ids, profile_info = profile)
    else:
        return redirect(url_for("login"))
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
    session.pop("user", None)
    session.pop("password", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
'''
plan:
take user name and password
use the login creds to link to the insta api
display data
'''