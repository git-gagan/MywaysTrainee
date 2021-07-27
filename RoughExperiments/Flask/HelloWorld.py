#Importing Flask module from flask package
from flask import Flask, render_template, request
import os

#Making an object which will be our WSGI app
app = Flask(__name__)
pic = os.path.join("static/r.png")

#Assign a URL route (telling the flask app when to call the view function)
#A URL route is associated with each view function
@app.route("/")
#create a view function so that something gets shown in the browser
def hello():
    #return "Hello World, I am New to FLASK!"
    return render_template("home.html")

@app.route("/Registration")
def register():
    return render_template("register.html")

@app.route("/confirmation", methods = ["Get","Post"]) #Specify methods get and post so as to use them
def confirm():
    #use flask request to get the data from the tmeplates
    if request.method == "POST":
        n = request.form.get("Name")
        c = request.form.get("City")
        p = request.form.get("Pnum")
    return render_template("confirm.html", name = n, city = c, num = p, image = pic) #Passing data to jinja2

#Run the application in main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 3000, debug=True) #Host to make it available across the network




