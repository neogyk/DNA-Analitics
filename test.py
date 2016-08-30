import os
from app import database_connection,config

from app import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        #with app.app_context():
         #   database_connection.init_db()
    def test_db(self):
        with app.app_context():
            from app import model,db
            user = model.Users('ledidukh','ledidukh','Leonid','Didukh')
            db.session.add(user)
            db.session.commit()
    def user_db(self):
        with app.app_context():
            from app import model,db
            users = model.Users.query.all()
            print users
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()