# allows MODEL to talk to database #
from flask_app.config.mysqlconnection import connectToMySQL

# allows us to flash messages on HTML pages #
from flask import flash, redirect, request

import os
print( os.environ.get("movie_api_key") )

# allows use of global DATABASE variable #
from flask_app import DATABASE


class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# classmethods here #

    # classmethod to create a favorite #
    @classmethod
    def new_fav(cls, data):
        query = 'INSERT INTO favorites (user_id, movie_id, title, created_at, updated_at)'
        query += 'VALUES (%(user_id)s, %(movie_id)s, %(title)s, NOW(), NOW());'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    # classmethod to get one favorite #
    @classmethod
    def get_one_favorite(cls, data):
        query = 'SELECT * FROM favorites WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])


    # classmethod to check if already favorited #
    @classmethod
    def check_fav(cls, data):
        query = 'SELECT * FROM favorites WHERE movie_id = %(movie_id)s AND user_id = %(user_id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return True


    # classmethod to get all favorites #
    @classmethod
    def get_all_favs(cls):
        query = 'SELECT * FROM favorites;'
        result = connectToMySQL(DATABASE).query_db(query)
        data = []
        for row in result:
            data.append(cls(row))
        return data

    #class method to remove a favorite #
    @classmethod
    def delete_fav(cls, data):
        query = 'DELETE FROM favorites WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result