from app import app,db,config
from app.config import SQLALCHEMY_DATABASE_URI
from app.config import SQLALCHEMY_MIGRATE_REPO
db.create_all()
