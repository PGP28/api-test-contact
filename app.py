from flask import Flask, request, jsonify, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Contact

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@app.route('/')
def root():
    return render_template('index.html')

@app.route("/api/contacts", methods=['GET', 'POST'])
@app.route("/api/contacts/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def contacts(id = None):
    if request.method == 'GET':
        if id is not None:
            contact = Contact.query.get(id)
            if contact:
                return jsonify(contact.serialize()), 200
            else:
                return jsonify({"msg": "Contact not found"}), 404
        else:
            contacts = Contact.query.all()
            contacts = list(map(lambda contact: contact.serialize(), contacts))
            return jsonify(contacts), 200

    if request.method == 'POST':
        pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass

if __name__ == "__main__":
    manager.run()