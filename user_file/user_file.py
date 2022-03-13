import os
from flask import request, redirect, url_for
import uuid
import datetime
from uuid import uuid4
from werkzeug.utils import secure_filename
from databaseconfig import filecol, repo
import re


class User_file:
    def upload(self, file):
        timestamp = datetime.datetime.now()
        id = uuid.uuid4()
        name = str(id).split("-")[0] + "".join(re.split('[-:\.\s]', str(timestamp))) + ".txt"
        upload = {
            "_id": id.hex,
            "name": name,
            "original name": file.filename,
            "timestamp": timestamp,
        }
        filecol.insert_one(upload)
        filename = secure_filename(file.filename)
        path = os.path.join(repo, filename)
        file.save(path)
        os.rename(path, os.path.join(repo, name))
        return redirect(url_for('dashboard'))

