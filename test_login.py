import os
from app import config
import database_connection

from app import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    def test_db(self):
        with app.app_context():
            from app import model,db
            user = model.Users('ledidukh','ledidukh','Leonid','Didukh')
            db.session.add(user)
            db.session.commit()
            db.session.close()
    
    def Authentification(self,login,password):
        with app.app_context():
            from app import model,db
            user = model.Users.query.filter(model.Users.login == login)
            if user:
                if user[0].check_password(password):
                    return True
    def test_users(self):
        print self.Authentification("ledidukh","ledidukh")
        print self.Authentification("1223123","123123123")
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()