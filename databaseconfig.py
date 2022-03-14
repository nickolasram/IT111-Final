import pymongo

client = pymongo.MongoClient('localhost', 27017)

# User Database
userdb = client.user_login_system
usercol = userdb.users

# File Database
filedb = client.file_objects
filecol = filedb.files


# File Repo
repo = 'text_files_repo'