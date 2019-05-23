from flask import Flask, render_template, request, jsonify
from services.marvel_services import search, search_DB, create_hyperlinks
from infra.db import cria_db
from infra.login_api import *
from infra.characters import characters_list

marvel_app = Flask(__name__)

@marvel_app.route('/marvel', methods = ['GET'])
def home():
    return render_template('search.html')

@marvel_app.route('/marvel', methods = ['POST'])
def search_character():

    char = request.form['character_name']
    char = search_DB(char)

    if len(char) == 1:
        search_list = search(char[0][0])
        return render_template('results.html', results = search_list[2], name = search_list[0], thumbnail = search_list[1])

    else:
        hyperlinks = create_hyperlinks(char)
        return render_template('search.html', hyperlinks = hyperlinks)



@marvel_app.route('/marvel/random', methods = ['GET'])
def random_character():
    pass

cria_db()
characters_list(ts, api_key, hash_key)

if __name__ == "__main__":
    marvel_app.run()
