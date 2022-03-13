from flask import Flask, Blueprint
from user.models import User

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")

@second.route('/signup', methods=['POST'])
def signup():
  return User().signup()

@second.route('/signout')
def signout():
  return User().signout()

@second.route('/login', methods=['POST'])
def login():
  return User().login()
