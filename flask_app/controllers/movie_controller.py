import requests
import random
from flask_app import app
from flask import jsonify, session, redirect, request, flash, json, render_template
from flask_app.models.favorite_model import Favorite
from flask_app.models.user_model import User
from flask_app.models.queue_model import Queue
import os


# # for loop to iterate dict and object #
# for movie in data['results']:
#     print(movie['id'])
#     print(movie['poster_path'])
#     print(movie['title'])
#     print(movie['release_date'])
#     print(movie['vote_average'])
#     print(movie['overview'])

# this is the front half of the poster path url to use in template rendering #
# https://image.tmdb.org/t/p/w500{POSTER PATH}

# create controller and have js fetch the data by calling controller app.route #
@app.route('/api/show_movie')
def api_show_movie():
    page = session['api_num']
# this is the discover movie variable with http request and my API key #
    discover = f'https://api.themoviedb.org/3/discover/movie?api_key={os.environ.get("movie_api_key")}&page=' + str(page)
# set get request to var response, passing in discover url in as url #
    response = requests.get(url = discover)
# set json response to var data to pass through for loop #
    data = response.json()
    return jsonify(data)


# approute to get new movies #
@app.route('/api/new_movies')
def api_new_movies():
    session['api_num'] = random.randrange(1, 500)
    return redirect('/random_movie')

# approute to show Movie Card #
@app.route('/show_detail/<int:id>')
def show_movie_card(id):
    if 'user_id' not in session:
        return redirect('/')
    session['movie_id'] = id
    return render_template('show_detail.html')

# API approute to show individual favorited movie #
@app.route('/api/show_detail')
def api_show_detail():
    movie_id = session['movie_id']
    discover = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.environ.get("movie_api_key")}&language=en-US'
    response = requests.get(url = discover)
    data = response.json()
    print(movie_id)
    return jsonify(data)

