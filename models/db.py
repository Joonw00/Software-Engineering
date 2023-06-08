import ssl
import pymongo

cluster = pymongo.MongoClient("mongodb+srv://joonwoo:p5628!pshp@cluster0.9hk9scr.mongodb.net/?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
DB = cluster["software_engineering"]
# users_collection = DB["users"]

def init_db(app):
    cluster.init_app(app)

