from survey_app.config.MySQLConnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, id, name, location, language, comments, created_at, updated_at):
        self.id = id
        self.name = name
        self.location = location
        self.language = language
        self.comments = comments
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_info( cls, data ):
        query = "INSERT into surveys (name,location,language,comments) VALUES (%(name)s,%(location)s,%(language)s,%(comments)s);"
        result = connectToMySQL('dojo_survey_db').query_db( query,data )
        return result

    # @classmethod
    # def get_last_survey(cls):
    #     query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
    #     results = connectToMySQL('dojo_survey_db').query_db(query)
    #     return results