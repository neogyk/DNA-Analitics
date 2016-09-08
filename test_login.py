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
    def test_tasks_db(self):
        with app.app_context():
            from app import model,db
            task = model.Tasks(name="FX",shot="SHOT_010",seq='020',reel='Reel_01',start_date='123/123/123',end_date='22/222/1223',duration='22.0')
            WorkFlow = model.WorkFlow(status="Approved",fill_date='11/22/1232',task =task)
            db.session.add(task)
            db.session.add(WorkFlow)
            db.session.commit()  
            db.session.close()   
    def user_db(self):
        with app.app_context():
            from app import model,db
            users = model.Users.query.all()
            print users
    def task_db(self):
        with app.app_context():
            from app import model,db
            tasks = model.Tasks.query.all()
            print tasks
            workflows = model.WorkFlow.query.all()
            print workflows
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()