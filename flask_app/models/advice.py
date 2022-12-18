from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask import flash,session
from flask_app.models import user

class Advice:
    DB = 'group_project'

    def __init__(self, data):
        self.id = data['id']
        self.user_advice = data['user_advice']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.advicer = None  # this for create instance of user

    #CREATE____MODEL____SQL
    @classmethod
    def create_advice(cls,data):
        query="""
            INSERT INTO advices (user_advice,user_id)
            VALUES (%(user_advice)s,%(user_id)s)
            ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("############## create query result",result)
        return result


    #get all advices in db 
    @classmethod
    def get_all_advices(cls):
        query="""
        SELECT * FROM advices
        JOIN users
        ON advices.user_id=users.id
        ;"""
        result=connectToMySQL(cls.DB).query_db(query)
        print("//////////////////",result)#this will give me list of dictionary which has all users info and their advices
        all_advices=[]#create empty list to append all adventures and users info to it
        if not result:
            return result
        for this_advice in result:
            new_advice=cls(this_advice)#create instance of reports and it will ignor user thats why we need to create dictionary for users table info
            user_data={
                'id':this_advice['users.id'],
                'first_name':this_advice['first_name'],
                'last_name':this_advice['last_name'],
                'email':this_advice['email'],
                'password':this_advice['password'],
                'user_image':this_advice['user_image'],
                'created_at':this_advice['users.created_at'],
                'updated_at':this_advice['users.updated_at'],
            }
            new_advice.advicer=user.User(user_data)#go to user class and pass users data to get instance of user and save it into new_adventure.creator
            all_advices.append(new_advice)
        return  all_advices
    
        #UPDATE____MODEL____SQL

    @classmethod
    def update_advice_by_id(cls,data):
        query="""
        UPDATE advices SET user_advice=%(user_advice)s
        WHERE id=%(id)s
        ;"""
        result= connectToMySQL(cls.DB).query_db(query,data)
        print("5555555555555555",result)
        return result

    #DELETE____MODEL____SQL
    @classmethod
    def delete_advice(cls,id):
        data={
            'id':id
        }
        query="""
        DELETE FROM advices WHERE id=%(id)s
        ;"""
        return connectToMySQL(cls.DB).query_db(query,data)