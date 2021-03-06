from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from databaseconfig import usercol
import uuid

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "password": request.form.get('password'),
      "uploads": []
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing name
    if usercol.find_one({ "name": user['name'] }):
      return jsonify({ "error": "Name already in use" }), 400

    if usercol.insert_one(user):
      return self.start_session(user)

    return jsonify({"error": "Signup failed"}), 400

  def signout(self):
    session.clear()
    return redirect('/')

  def login(self):

    user = usercol.find_one({
      "name": request.form.get('name')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)

    return jsonify({ "error": "Invalid login credentials" }), 401
