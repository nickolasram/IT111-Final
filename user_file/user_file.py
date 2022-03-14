import os
from flask import request, redirect, url_for, session
import uuid
import datetime
from uuid import uuid4
from werkzeug.utils import secure_filename
from databaseconfig import filecol, repo, usercol
import re


class User_file:
    def upload(self, file):
        timestamp = datetime.datetime.now()
        id = uuid.uuid4()
        original = file.filename
        author = session['user']['name']
        name = str(id).split("-")[0] + "".join(re.split('[-:\.\s]', str(timestamp))) + ".txt"
        upload = {
            "_id": id.hex,
            "name": name,
            "original name": original,
            "timestamp": timestamp,
            "author": author
        }
        filecol.insert_one(upload)
        filename = secure_filename(file.filename)
        path = os.path.join(repo, filename)
        file.save(path)
        os.rename(path, os.path.join(repo, name))
        usercol.updateOne(
            {"name": author},
            {"$push": {"uploads": (name, original, timestamp)}}
        )
        print(usercol.find({"name": author}))
        return redirect(url_for('dashboard'))

