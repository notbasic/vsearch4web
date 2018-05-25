from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'mad as hell'


@app.route('/now')
def newsy():
    return 'how now brown cow.'


@app.route('/search4')
def do_search() ->str:
    return str(search4letters('life, the univers, and everything','eiru,!'))

app.run()