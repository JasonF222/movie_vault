# allows MODEL to talk to database #
from flask_app.config.mysqlconnection import connectToMySQL

# allows us to flash messages on HTML pages #
from flask import flash, redirect, request

# allows use of global DATABASE variable #
from flask_app import DATABASE

import os
print( os.environ.get("movie_api_key") )

# allows Regular Expression for Validations #
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')



# Define a class #
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Classmethods here #


    @classmethod
    def new_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at)'
        query += 'VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result


    # classmethod to retrieve user by id #
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users where id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        # return the first row as a dictionary with data from selected user id #
        return cls(result[0])


    # classmethod to check if user email is in database #
    # if email does NOT exist, return False #
    # if email DOES exist, return the row with the user information #
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users where email = %(email)s'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        return cls(result[0])


    # Staticmethods here (staticmethods apply to instances of class, without affecting instance) #
    # Normally used for validation and to check data in class without changing data itself #

    # This method checks that all fields have something entered in #
    # flashes a message if there is nothing entered in the field #
    @staticmethod
    def validate_all_present(user):
        if not len(user['first_name']) > 0:
            flash('You must enter a  first name!')
            return False
        if not len(user['last_name']) > 0:
            flash('You must enter a last name!')
            return False
        if not len(user['email']) > 0:
            flash('You must enter an email!')
            return False
        if not len(user['pw']) > 0:
            flash('You must enter a password!')
            return False
        if not len(user['pw']) > 0:
            flash('You must confirm your password!')
            return False
        return True


    # This method validates name length and matching passwords #
    @staticmethod
    def validate_user(user):
        if not len(user['first_name']) >= 3:
            flash('First name must be at least 3 characters!')
            return False
        if not len(user['last_name']) >= 3:
            flash('Last name must be at least 3 characters!')
            return False
        if not user['pw'] == user['pw1']:
            flash('Passwords must match!')
            return False
        return True


    # This method will validate email (correct format, etc.) #
    @staticmethod
    def validate_email(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email Address!')
            is_valid = False
        return is_valid


    # This method checks if email is in database #
    # If email exists, user will not be able to create new account #
    @staticmethod
    def email_exist(user):
        if User.get_by_email(user):
            flash('Email is already in use!')
            return False
        return True