# Develop web application using Flask
# 1. Create py program named App.py
# 2. Make sure already inside the folder where the App.py is

# flask is a module
# inside it has a class call "Flask"
# lts import class Flask

from flask import Flask

# lets create an instance of the class Flask
# Flask class already have __init__ 
# the Flask class takes file thats going to be the main program as parameter

app = Flask(__name__)

# WSGI server is for development python

# IF THERES A REQUEST FOR "/", THEN EXECUTE
# which return Hello World

# @app.route("/")
# def say_hello():
#     return "Anati Comel"

@app.route("/products")
def say_hello():
    return ["apple", "orange", "banana"]


# inside browser -->> response