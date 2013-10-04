from __init__ import app
from models import *


@app.route('/')
def index():
	return ''


@app.route('/search', methods=['GET', 'POST'])
def search():
	return ''


@app.route('/document/add', methods=['POST'])
def document_add():
	return ''
