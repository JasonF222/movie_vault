import requests
import random
from flask_app import app
from flask import jsonify, session, redirect, request, flash, render_template
from flask_app.models.queue_model import Queue
import os
print( os.environ.get("movie_api_key") )

# approute to add to queue #
@app.route('/add_queue', methods=['POST'])
def add_queue():
    print(request.form)
    data = {
        'user_id': session['user_id'],
        'movie_id': request.form['movie_id'], 
        'title': request.form['title'], 
    }
    if Queue.check_queue(data):
        print('Already in Queue!')
        return redirect('/random_movie')    
    Queue.new_queue(data)
    return redirect('/random_movie')

# approute to view queue #
@app.route('/queue_list')
def show_queue():
    if not 'user_id' in session:
        return redirect('/')
    queues = Queue.get_all_queued()
    return render_template('queue_movie.html', queues = queues)


# API approute to show one movie in queue #
@app.route('/api/one_queue')
def api_one_queue():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('test.html')

# approute to delete a movie from queue #
@app.route('/delete_from_queue/<int:id>')
def delete_from_queue(id):
    if not 'user_id' in session:
        return redirect('/')
    Queue.delete_from_queue({'id': id})
    return redirect('/queue_list')
    
# approute to add to queue from favorites #
@app.route('/add_to_queue', methods=['POST'])
def add_to_queue():
    print(request.form)
    data = {
        'user_id': session['user_id'],
        'movie_id': request.form['movie_id'], 
        'title': request.form['title'], 
    }
    if Queue.check_queue(data):
        print('Already in Queue!')
        return redirect('/favorite_list')    
    Queue.new_queue(data)
    return redirect('/favorite_list')
