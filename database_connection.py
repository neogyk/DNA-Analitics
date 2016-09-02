from app import app,db,config
from app.config import SQLALCHEMY_DATABASE_URI
from app.config import SQLALCHEMY_MIGRATE_REPO
import os.path
db.create_all()
