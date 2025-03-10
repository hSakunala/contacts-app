# Contains all of the database models

from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    first_name= db.Column(db.String(80), unique= False, nullable= False)
    last_name= db.Column(db.String(80), unique= False, nullable= False)
    email= db.Column(db.String(120), unique= True, nullable= False)
    
    # take all model fields, convert to py dict, and then convert to json
    def to_json(self):
        # json nameing convention is camelcase
        return {
            "id" : self.id,
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "email": self.email,
        }