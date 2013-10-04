from pymongo import MongoClient

import sys, os

client = MongoClient(os.environ.get('DB_URI', 'mongodb://localhost:27017/'))
db = client.autumn
collection = db.document


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
