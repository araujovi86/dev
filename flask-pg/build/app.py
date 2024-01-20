import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import MethodNotAllowed
import socket
import time 


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PW')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PW')}@{os.getenv('DB_HOST')}:5432/{os.getenv('DB_NAME')}?sslmode=require&sslrootcert=/opt/app-root/src/ca.crt"
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

#@app.route('/write', methods=['POST'])
#def write_to_db():
    #data = request.get_json()
    #new_item = Item(name=data['name'])

    #with app.app_context():
        #db.session.add(new_item)
        #db.session.commit()

    #return jsonify({'message': 'Data written successfully!'})

@app.route('/write', methods=['GET'])
def write_to_db():
    if request.method != 'GET':
        raise MethodNotAllowed(valid_methods=['GET'])

    # Generate a random item name using the formula (IP of HTTP client + Server time)
    client_ip = request.remote_addr  # Get the IP of the HTTP client
    server_time = str(int(time.time()))  # Get the current server time
    random_item_name = f"{client_ip}_{server_time}"

    # Create a new Item and add it to the database
    new_item = Item(name=random_item_name)
    with app.app_context():
        db.session.add(new_item)
        db.session.commit()

    return jsonify({'message': 'Data written successfully!', 'item_name': random_item_name})


@app.route('/read')
def read_from_db():
    with app.app_context():
        items = Item.query.all()
        item_list = [{'id': item.id, 'name': item.name} for item in items]

    return jsonify({'items': item_list})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
