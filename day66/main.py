from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random_caffe():
    randomResult = db.select(Cafe).order_by(func.random())
    randomCaffe = db.session.scalars(randomResult).first()
    return jsonify(cafe=randomCaffe.to_dict())


@app.route("/all", methods=['GET'])
def all_caffe():
    randomCaffe = db.session.scalars(db.select(Cafe).order_by(Cafe.name)).all()
    all_cafes = [cafe.to_dict() for cafe in randomCaffe]
    return jsonify(cafes=all_cafes, count=len(all_cafes))


@app.route("/search", methods=['GET'])
def search():
    loc = request.args.get('loc', default='London', type=str)
    search_result = db.session.scalars(db.select(Cafe).where(Cafe.location.like(f'%{loc}%'))).all()
    if len(search_result) <= 0:
        return jsonify(error={
            'Not Found': 'Sorry, We could\'t find such location'
        }), 404
    else:
        all_cafes = [cafe.to_dict() for cafe in search_result]
        return jsonify(cafes=all_cafes, count=len(search_result))


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add():
    data = request.get_json(silent=True) or {}
    required_fields = ['name', 'map_url', 'img_url', 'loc', 'sockets',
                       'toilet', 'wifi', 'calls', 'seats', 'coffee_price']
    missing_fields = [field for field in required_fields if field not in data]
    if len(missing_fields) > 0:
        return jsonify({'error': f"Missing required fields: {', '.join(missing_fields)}"}), 400
    else:
        cafe = Cafe(
            name=data["name"],
            map_url=data["map_url"],
            img_url=data["img_url"],
            location=data["loc"],
            has_sockets=bool(data["sockets"]),
            has_toilet=bool(data["toilet"]),
            has_wifi=bool(data["wifi"]),
            can_take_calls=bool(data["calls"]),
            seats=data["seats"],
            coffee_price=data["coffee_price"],
        )
        try:
            db.session.add(cafe)
            db.session.commit()
            return jsonify({"success": "Successfully added the new cafe."})
        except IntegrityError as e:
            # 1. ALWAYS roll back the session when a database transaction fails
            db.session.rollback()
            # 2. Extract the underlying database error message
            error_details = str(e.orig)
            return jsonify({
                "error": "Database integrity violation",
                "details": error_details
            }), 400

        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({
                "error": "A database error occurred",
                "details": str(e)
            }), 500

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify({"error": f"Record with ID {cafe_id} does not exist"}), 404

    data = request.get_json(silent=True) or {}
    if 'new_price' not in data:
        return jsonify({'error': f"Missing new_price fields"}), 400
    else:
        cafe.coffee_price = data['new_price']
        db.session.commit()
        return jsonify({"message": "price updated successfully", "cafe": cafe.to_dict()})

# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify({"error": f"Record with ID {cafe_id} does not exist"}), 404
    api_key = request.args.get('api_key', type=str)
    print(api_key)
    if api_key != 'mySecretApiKey':
        return jsonify({"error": "Invalid api key."}), 401

    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"message": "cafe deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
