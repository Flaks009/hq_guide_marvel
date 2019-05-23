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

    char_form = request.form['character_name']
    offset_form = request.form['offset']
    char = search_DB(char_form)

    if len(char) == 1:
        search_list = search(char[0][0], int(offset_form))
        return render_template('results.html', results = search_list[2], name = search_list[0], thumbnail = search_list[1] , pages = search_list[3])

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
