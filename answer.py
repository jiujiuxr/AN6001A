from flask import Flask
from flask import render_template,request

answer=Flask(__name__)

@answer.route("/",methods=["GET","POST"])
def answer1():
    return(render_template("answer1.html"))

if __name__=="__answer1__":
    answer.run()