from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import...other model file name here
from flask import flash
import re # To use REGEX
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# class User:
#   def __init__(self, data):
        # self.id = data['id']
        # self.first_name = data['first_name']
        # self.last_name = data['last_name']
        # self.email = data['email']
        # self.password = data['password']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']
        # self.somethingElseThisClassMightContain = []
            # I.E. Dojos and Ninjas example, dojos has an empty list of ninjas

# CREATE
    # Make sure to indent when making a class method
    # @classmethod
    # def method_name(cls, data):
        # query = "INSERT INTO tableName (column_name1, column_name2...) VALUES (%(column_data1)s,..., NOW(), NOW())"
        # result = connectToMySQL('nameOfDB').query_db(query, data)
        # return result

# READ ALL:
    # @classmethod
        # Name your class method smartly
    # def get_all_plural_noun_here(cls):
        
        # Store your query and then type it out just like in the MySQL workbench:
    #   query = "SELECT * FROM column_name;"
    #   results = connectToMySQL('database_name').query_db(query)
        
        # Make a list:
    #   plural_noun = []

        # Run a for loop to populate the above list:
    #   for singlular_noun in plural_noun:      
        # plural_noun.append(cls(singular_noun))

        # Return that list, be careful of indentation
    #   # return plural_noun

# READ ONE:
#   @classmethod
#   def get_something_by_id/email(cls, data):
#       query = "SELECT * FROM tableName WHERE email/id = %(email/id)s;"
#       result = connectToMySQL('database_name').query_db(query, data)
#       if result:
#           return cls(result[0])
#       return None

# UPDATE

# DELETE
    # @classmethod
    # def delete_SOMETHING(cls, SOMETHING_id):
    #   query = "DELETE FROM tableName WHERE id = %(SOMETHING_id)s;"
    #   data = {
    #       "SOMETHING_id": SOMETHING_id
    #   }
    #   return connectToMySQL('database_name').query_db(query, data)

# VALIDATION
#   @staticmethod
#   def validate(singularParameter, probably a lowercase version of this class)
#       is_valid = True
#       query = "SELECT * FROM tableName WHERE email = %(email)s;" <--- for checking to see if an email exists in DB already
#       existing_...probably_email = connectToMySQL('database_name').query_db(query, singularParameter...same as above)
#       if...(singularParameter['first_field']) < / <= / == / etc.:
#       flash("Your message here")
#       is_valid = False (DON'T FORGET THIS)!
#       
#       Name checks:
#       if len(variable_from_above['first_name']) < 2:
#           flash("First name must be at least 2 letters", category = 'match_this_with_what's_in_html_section')
#            is_valid = False

#       Email checks (format and existing in DB):
#       if not EMAIL_REGEX.match(variable_from_above['email']):
#           flash("...", category = '')
#           is_valid = False
#       if len(existing_SOMETHING..probably_email) >= 1
#           flash("This email is...", category = '')
#            is_valid = False

#       Password checks: (length is the same, just include it)
#       if variable_from_above['password'] != variable_from_above['confirm_pw']:
#           flash("...", category = '')
#           is_valid = False
#   return is_valid