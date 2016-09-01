from app import db
 
class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    login = db.Column(db.String(64))
    password  = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    def __init__(self,login,password,first_name,second_name):
        self.first_name = first_name
        self.login = login
        self.password = password
        self.second_name = second_name
    def __repr__(self):
        print "User %r %r %r %r" % (self.login,self.password,self.first_name,self.second_name)
class Tasks(db.Model):

    task_id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(64))
    shot = db.Column(db.String(64))
    seq = db.Column(db.String(64))
    reel = db.Column(db.String(64))
    start_date = db.Column(db.String(64))
    end_date = db.Column(db.String(64))
    duration = db.Column(db.String(64))
    def __init__(self,name,shot,seq,reel,start_date,end_date,duration):
        self.name = name
        self.shot = shot
        self.seq = seq
        self.reel = reel
        self.start_date = start_date
        self.end_date = end_date
        self.duration = duration
    def __repr__(self):
        print "Task %r %r %r %r %r %r %r " % (self.name,self.shot,self.seq,self.reel,self.start_date,self.end_date,self.duration)
class WorkFlow(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    status = db.Column(db.String(64))
    fill_date = db.Column(db.String(64))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.task_id'))
    task = db.relationship('Tasks',
        backref=db.backref('workflow', lazy='dynamic'))
    def __init__(self,status,fill_date,task):
        self.status = status
        self.fill_date = fill_date
        self.task = task
    def __repr__(self):
        print "work_flow %r %r" % (self.status,self.task_id)