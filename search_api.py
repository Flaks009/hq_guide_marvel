from flask import Flask, render_template, request, jsonify
from services.marvel_services import search, search_DB, create_hyperlinks, randomize
from infra.db import cria_db
import random
import os


marvel_app = Flask(__name__)



@marvel_app.route('/', methods = ['GET'])
def search_page():
    return render_template('search.html')

@marvel_app.route('/', methods = ['POST'])
def search_character():

    char_form = request.form['character_name']
    offset_form = request.form['offset']
    char = search_DB(char_form)

    if len(char) == 1:
        search_list = search(char[0][0], int(offset_form))
        return render_template('results.html', results = search_list[2], name = search_list[0], thumbnail = search_list[1] , pages = search_list[3])

    elif len(char) == 0:
        hyperlinks = 0
        return render_template('search.html', hyperlinks = hyperlinks)

    else:
        hyperlinks = create_hyperlinks(char)
        return render_template('search.html', hyperlinks = hyperlinks)



@marvel_app.route('/random', methods = ['POST'])
def random_character():

    randomId = random.randint(1, 1491)
    print(randomId)
    offset_form = request.form['offset']
    char = randomize(randomId)

    if len(char) == 1:
        search_list = search(char[0][0], int(offset_form))
        return render_template('results.html', results = search_list[2], name = search_list[0], thumbnail = search_list[1] , pages = search_list[3])

    else:
        hyperlinks = create_hyperlinks(char)
        return render_template('search.html', hyperlinks = hyperlinks)


cria_db()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    marvel_app.run(host='0.0.0.0', port=port)
