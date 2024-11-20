from flask import Flask
from flask import render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("answer1&2.html"))

if __name__=="__main__":
    app.run()