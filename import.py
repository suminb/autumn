import os, sys
import requests

for line in sys.stdin.readlines():
    params = dict(
        source='en',
        target='ko',
        source_text=line,
        target_text='',
    )
    requests.post('http://localhost:5000/document', data=params)

