import pymongo

cluster = pymongo.MongoClient("mongodb+srv://joonwoo:p5628!pshp@cluster0.9hk9scr.mongodb.net/?retryWrites=true&w=majority")
DB = cluster["software_engineering"]

def init_db(app):
    cluster.init_app(app)
