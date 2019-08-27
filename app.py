""" Flask app for Feedback """

from Flask import flask, render_template, redirect, flash  # jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, User
from forms import RegisterForm, LoginForm

# add all the routes here
# GET / redirects to /register

# GET /register shows form that will register/create a user

# POST /register

# GET /login

# POST /login

# GET /secret
