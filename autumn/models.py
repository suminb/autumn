from pymongo import MongoClient, ASCENDING, DESCENDING
from bson.objectid import ObjectId
from json import JSONEncoder
from datetime import datetime

import sys, os

client = MongoClient(os.environ.get('DB_URI', 'mongodb://localhost:27017/'))
db = client.autumn

class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        else:            
            return JSONEncoder.default(obj, **kwargs)


# class Fingerprint(db.Model, BaseModel):
#     document_id = db.Column(UUID, primary_key=True)
#     fingerprint = db.Column(db.Integer, primary_key=True)
#     offset = db.Column(db.Integer, primary_key=True)


# class Document(db.Model, BaseModel):
#     id = db.Column(UUID, primary_key=True)
#     timestamp = db.Column(db.DateTime(timezone=True))
#     source = db.Column(db.String(16))
#     target = db.Column(db.String(16))
#     source_text = db.Column(db.Text)
#     target_text = db.Column(db.Text)

if __name__ == '__main__':
    db.document.create_index([('source', ASCENDING), ('target', ASCENDING)])
    db.document.create_index([('fingerprint.digest', ASCENDING)])
