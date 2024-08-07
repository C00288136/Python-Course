from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

API_KEY='TopSecretAPIKey'
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(response={"Success": "Successfully added the new cafe"})

# HTTP PUT/PATCH - Update Record

@app.route('/update-price/<cafe_id>')
def update_coffee_price(cafe_id):
    cafe = db.get_or_404(Cafe,cafe_id)
    if cafe:
            
        updated_price = request.args.get("new_price")
        cafe.coffee_price = updated_price
        db.session.commit()
        return jsonify({"Success" : "Price has been changed"})
    return jsonify({"error" : "Cafe not found"})
    

# HTTP DELETE - Delete Record

@app.route('/report-closed/<cafe_id>', methods=["DELETE"])
def report_closed(cafe_id):
    api = request.args.get('api_key')
    if api == API_KEY:
        cafe = db.get_or_404(Cafe,cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"Success" : "The cafe has been deleted"}), 200
        else:
            return jsonify({"Error" : "This cafe id doesn't exists"}), 404
    else:
        return jsonify(Error={'error': "Sorry you have the wrong api key"}),401

@app.route("/random", methods=['GET'])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())
    

@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    # using list comprehension to turn each cafe into a dictionary entry
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    
@app.route('/search')
def search_loc():
    query_location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    cafes_listed = result.scalars().all()
    if cafes_listed:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_listed])
    return jsonify(error={
                   "Not Found" : "Sorry we dont have a cafe at that location"}), 404
    
    


if __name__ == '__main__':
    app.run(debug=True)
