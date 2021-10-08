from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@localhost/empfynd'
db = SQLAlchemy(app)


class Car(db.Model):
    model_id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Car(name = {Car.name}, color = {Car.color}, price = {Car.price})"


#db.create_all()

car_put_args = reqparse.RequestParser()

car_put_args.add_argument("model_id", type=int, help="model of the car is required", required=True)
car_put_args.add_argument("count", type=int, help="count of the car", required=True)
car_put_args.add_argument("name", type=str, help="name of the car", required=True)
car_put_args.add_argument("color", type=str, help="color of the car is required", required=True)
car_put_args.add_argument("price", type=int, help="price of the car is required", required=True)


car_update_args = reqparse.RequestParser()
car_update_args.add_argument("count", type=int, help="count of the car is required")
car_update_args.add_argument("price", type=int, help="price of the car")


resource_fields = {
    'model_id': fields.Integer,
    'name': fields.String,
    'color': fields.String,
    'count': fields.Integer,
    'price': fields.Integer
}


class ShowRoom(Resource):
    @marshal_with(resource_fields)
    def get(self, model_id):
        result = Car.query.filter_by(model_id=model_id).first()
        if not result:
            abort(404, message="Could not find car with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, model_id):
        args = car_put_args.parse_args()
        result = Car.query.filter_by(model_id=model_id).first()
        if result:
            # print(result)
            abort(501, message="update the car count")

        car = Car(model_id=args['model_id'], count=args['count'], name=args['name'], color=args['color'], price=args['price'])
        db.session.add(car)
        db.session.commit()
        return car, 201

    @marshal_with(resource_fields)
    def patch(self, model_id):
        args = car_update_args.parse_args()
        result = Car.query.filter_by(model_id=model_id).first()
        if not result:
            abort(404, message="Car doesn't exist, cannot update")
        if args['count']:
            result.count = args['count']
        if args['price']:
            result.price = args['price']
        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, model_id):
        # args = car_update_args.parse_args()
        result = Car.query.filter_by(model_id=model_id).first_or_404(description="ye car hai ni")
        # if args['count'] > result.count:
        #     return f"purchase limit exceeded--only--{result.count} car is left", 409
        # result.count = result.count - args['count']
        # if result.count == 0:
        db.session.delete(result)
        db.session.commit()
        return result


api.add_resource(ShowRoom, "/car/<int:model_id>")

if __name__ == "__main__":
    app.run(debug=True)
