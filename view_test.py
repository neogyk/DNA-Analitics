import os
from app import config
import database_connection
from app import view
from app import app
import unittest
import tempfile
import json
from app import jsonify


class FlaskrViewTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        #with app.app_context():
         #   database_connection.init_db()
  
    def test_unauth_login(self):
        rv = self.app.post('/login/valid',jsonify({'login':"user",'password':"123qweASD"}))
        print rv
    def test_refistration(self):
        rv = self.app.post('login/register',jsonify({'login':"user",'password':"123qweASD"}))
        print rv
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()