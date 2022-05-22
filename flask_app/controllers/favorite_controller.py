import requests
import random
from flask_app import app
from flask import jsonify, session, redirect, request, flash, render_template
from flask_app.models.favorite_model import Favorite

import os
print( os.environ.get("movie_api_key") )

# approute to add to favorites #
@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    print(request.form)
    data = {
        'user_id': session['user_id'],
        'movie_id': request.form['movie_id'], 
        'title': request.form['title'], 
    }
    if Favorite.check_fav(data):
        print('Favorite Exists!')
        return redirect('/random_movie')    
    Favorite.new_fav(data)
    return redirect('/random_movie')

# approute to view favorites #
@app.route('/favorite_list')
def show_favorite():
    if not 'user_id' in session:
        return redirect('/')
    favorites = Favorite.get_all_favs()
    print(favorites)
    return render_template('favorite_movie.html', favorites = favorites)


# API approute to show one favorite #
@app.route('/api/one_favorite')
def api_one_favorite():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('test.html')


# approute to delete a favorite #
@app.route('/delete_favorite/<int:id>')
def delete_favorite(id):
    if not 'user_id' in session:
        return redirect('/')
    Favorite.delete_fav({'id': id})
    return redirect('/favorite_list')


# approute to add to favorites #
@app.route('/add_to_favorite', methods=['POST'])
def add_to_favorite():
    print(request.form)
    data = {
        'user_id': session['user_id'],
        'movie_id': request.form['movie_id'], 
        'title': request.form['title'], 
    }
    if Favorite.check_fav(data):
        print('Favorite Exists!')
        return redirect('/queue_list')    
    Favorite.new_fav(data)
    return redirect('/queue_list')