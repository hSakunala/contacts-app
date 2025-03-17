# Contains the main roots/endpoints CRUD- create,read,update,delete
from flask import request, jsonify
from config import app, db
from models import Contact

# a '@' line is a decorator
@app.route("/contacts", methods= ["GET"])
def get_contacts():
    # get all contacts (python objects)
    contacts = Contact.query.all()
    
    #use lambda to convert each contact with to_json
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    
    # jsonify converts python objects (like lists or dicts) into json
    return jsonify({"contacts": json_contacts})
    
    
    
@app.route("/create_contact", methods= ["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    # check if all fields are not null
    if not first_name or not last_name or not email:
        return (jsonify({"message" : "You must include a first name, last name, and email"}), 
                400,
        )
    
    # create new contact with Conctact Class 
    new_contact = Contact(first_name= first_name, last_name = last_name, email = email)
    try:
        # add to db session (still in staging area)
        db.session.add(new_contact)
        # commit to the db (now offically in db)
        db.session.commit()  
    except Exception as e:
        return jsonify({"message" :str(e)}), 400
    
    return jsonify({"message" : "User created!"}), 201


# specify path paramaeter user_id
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message" : "User not found"}), 404
    
    # data user inputs to update existing user
    data = request.json
    
    # change to firstName, if no firstName is in new json data default to original firstName
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    # since the contact already existed in session, can just commit new changes
    db.session.commit()
    
    return jsonify({"message" : "User updated."}), 200
    
        
# Delete contact
@app.route("/delete_contact/<int:user_id>", methods= ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message" : "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message" : "User deleted."}), 200
        
if __name__ == "__main__":
    with app.app_context():
        # create all of the models defined in db if not already created
        db.create_all()
    
    app.run(debug=True)