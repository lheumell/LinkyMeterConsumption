import pymongo 
import math

# define the client, the database, and the collection
# the database and the collection are created at first insert 
# if needed
client = pymongo.MongoClient('localhost',27017)
mydb = client["test2"]
sinfun = mydb["sin2"]
