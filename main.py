from flask import Flask , render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
#import os for making a database in currently file
import os
#start to make an app
app = Flask(__name__)
#making database
file_dir = os.path.dirname(os.path.abspath(__file__))
goal_route = os.path.join(file_dir,"app.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + goal_route

db=SQLAlchemy(app)
#define product and shopping cart models
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    image_path = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    def making_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_path': self.image_path,
            'price': self.price,
        }

class Shopping_Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def making_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }