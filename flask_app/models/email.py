from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.email = data['email']

    @classmethod
    def add_an_email(cls, data):
        query = "INSERT INTO emails (name, updated_at, created_at) VALUES (%(name)s, now(), now())"
        return connectToMySQL('emailassignment').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        if len(email['name']) < 4:
            flash('Email must be longer than 3 characters')
            is_valid = False
        if not EMAIL_REGEX.match(email['name']):
            flash('Invalid email address!')
            is_valid = False
        return is_valid

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        return connectToMySQL('emailassignment').query_db(query)
        