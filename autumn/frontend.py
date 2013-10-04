from flask import request, jsonify
from datetime import datetime
from winnow import winnow

from __init__ import app
from models import *

import json


@app.route('/search', methods=['GET', 'POST'])
def search():

    query = request.args['query']

    fingerprint = list(winnow(query))

    cursor = db.document.find({'fingerprint.digest': fingerprint[0][1]})

    return json.dumps(map(None, cursor), cls=MongoEncoder)


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
        fingerprint=[dict(offset=v[0], digest=v[1]) for v in winnow(source_text)]
    )
    document_id = db.document.insert(document)

    return ''
