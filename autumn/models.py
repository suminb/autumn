from flask.ext.sqlalchemy import SQLAlchemy

from __init__ import app

db = SQLAlchemy(app)

def serialize(obj):
    import json
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data) # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields


class BaseModel:
    def serialize(self):
        payload = serialize(self)

        for id_field in ('id', 'user_id', 'request_id', 'response_id'):
            if hasattr(self, id_field) and getattr(self, id_field) != None:
                value = uuid.UUID(getattr(self, id_field)).int
                payload[id_field] = base62.encode(value)

        return payload

    @classmethod
    def insert(cls, commit=True, **kwargs):
        record = cls()

        if hasattr(record, 'id'): record.id=str(uuid.uuid4())
        if hasattr(record, 'timestamp'): record.timestamp = datetime.now()

        for key, value in kwargs.iteritems():
            setattr(record, key, value);

        db.session.add(record)
        if commit: db.session.commit()

        return record


class Fingerprint(db.Model, BaseModel):
	document_id = db.Column(UUID, primary_key=True)
	fingerprint = db.Column(db.Integer, primary_key=True)
	offset = db.Column(db.Integer, primary_key=True)


class Document(db.Model, BaseModel):
    id = db.Column(UUID, primary_key=True)
	timestamp = db.Column(db.DateTime(timezone=True))
	source = db.Column(db.String(16))
    target = db.Column(db.String(16))
    source_text = db.Column(db.Text)
    target_text = db.Column(db.Text)
