import pandas as pd 
import os
#Configure the files
dataPath = "\EDIT\TotalStatistics"
os.path.listdir(dataPath)
import sqlalchemy
engine = create_engine('sqlite://app.db', echo=False)
#try to map one csv
df = pd.open_csv("C:\Users\i.podmokov\Desktop\Info Flask\EDIT\TotalStatistics\31.05.2016\REEL_01.csv")