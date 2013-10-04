from flask import request
from datetime import datetime
from winnow import winnow

from __init__ import app
from models import *

@app.route('/')
def index():
    return ''


@app.route('/search', methods=['GET', 'POST'])
def search():
    return ''


@app.route('/document', methods=['POST'])
def document_add():
    source, target, source_text, target_text = map(lambda x: request.form[x],
        ('source', 'target', 'source_text', 'target_text'))

    # TODO: Any better way to handle this?
    document = dict(
        timestamp=datetime.utcnow(),
        source=source,
        target=target,
        source_text=source_text,
        target_text=target_text,
    )
    document_id = db.document.insert(document)

    for wh in winnow(source_text):
        fingerprint = dict(
            document_id=document_id,
            digest=wh[1],
            offset=wh[0],
        )

        db.fingerprint.insert(fingerprint)

    return ''
