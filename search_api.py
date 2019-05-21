from flask import Flask, render_template, request, jsonify
from services.marvel_services import search

marvel_app = Flask(__name__)

@marvel_app.route('/marvel', methods = ['GET'])
def home():
    return render_template('search.html')

@marvel_app.route('/marvel', methods = ['POST'])
def search_character():

    char = request.form['character_name']
    search_list = search(char)

    return render_template('results.html', search_list = search_list)

@marvel_app.route('/marvel/random', methods = ['GET'])
def random_character():
    pass


if __name__ == "__main__":
    marvel_app.run()
