# allows MODEL to talk to database #
from flask_app.config.mysqlconnection import connectToMySQL

# allows us to flash messages on HTML pages #
from flask import flash, redirect, request

import os


# allows use of global DATABASE variable #
from flask_app import DATABASE


class Queue:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# classmethods here #

    # classmethod to create a Queue #
    @classmethod
    def new_queue(cls, data):
        query = 'INSERT INTO queues (user_id, movie_id, title, created_at, updated_at)'
        query += 'VALUES (%(user_id)s, %(movie_id)s, %(title)s, NOW(), NOW());'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    # classmethod to check if already in queue #
    @classmethod
    def check_queue(cls, data):
        query = 'SELECT * FROM queues WHERE movie_id = %(movie_id)s AND user_id = %(user_id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return True


    # classmethod to get all queued movies #
    @classmethod
    def get_all_queued(cls, data):
        query = 'SELECT * FROM queues WHERE user_id = %(user_id)s ORDER BY id DESC;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        userQueue = []
        for row in result:
            userQueue.append(cls(row))
        return userQueue

    # classmethod to get all queued movies A-Z #
    @classmethod
    def get_all_queued_ascend(cls, data):
        query = 'SELECT * FROM queues WHERE user_id = %(user_id)s ORDER BY title;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        userQueue = []
        for row in result:
            userQueue.append(cls(row))
        return userQueue

    # classmethod to get all queued movies Z-A #
    @classmethod
    def get_all_queued_descend(cls, data):
        query = 'SELECT * FROM queues WHERE user_id = %(user_id)s ORDER BY title DESC;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        userQueue = []
        for row in result:
            userQueue.append(cls(row))
        return userQueue

    #class method to remove a movie from queue #
    @classmethod
    def delete_from_queue(cls, data):
        query = 'DELETE FROM queues WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result