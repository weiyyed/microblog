import os
class Config():
# CSRF_ENABLED = True
    SECRET_KEY =os.environ.get("SECRET_KEY") or  'you-will-never-guess'