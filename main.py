from flask import Flask , render_template,url_for,request
#start to make an app
#make a simple list to use it as database
l=[
    {"product":"Samsung A50", "price":"9500000","link":""},
    {"product":"Samsung A72", "price":"18600000","link":""},
    {"product":"Samsung A32", "price":"11600000","link":""},
    {"product":"Samsung A23", "price":"7200000","link":""},
    {"product":"Samsung A52s", "price":"19000000","link":""}
]
app = Flask(__name__)
#start the real thing
