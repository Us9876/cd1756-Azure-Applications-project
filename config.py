import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cwT8Q~uIQjOgdc.J9PQRsuhCLGujVT7teCiLLab0'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'testcms2'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'vhgpyF+ei5EC8/q4OrfY3XyBLPzt0Pm70xV8Gq5lmUGKXjeRFlTkBObxFO52UnZG2xAHwHz9GfWS+AStUkP84Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'testcms1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'testcms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'testcmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'test@123admin'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "8ccb0c34-4ef0-40d8-b900-87ec1593584b"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "508907ce-c060-4a6b-ac87-44c9cf2c079d"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
