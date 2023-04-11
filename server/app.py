from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Lease, Apartment, Tenant

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///apartments.db'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

migrate = Migrate( app, db )
db.init_app( app )
api = Api(app)

class Home(Resource):
    def get(self):
        return "Good Morning"
    
api.add_resource(Home, '/')

class Apartments(Resource):
    def get(self):
        home = Apartment.query.all()
        home_list = []
        for h in home:
            h_dict = {
                "id": h.id,
                "number": h.number
            }
            home_list.append(h_dict)
        return make_response(jsonify(home_list), 200)
    
    def post(self):
        data = request.get_json()
        try:
            new_home = Apartment(
                number = data['number']
            )
            db.session.add(new_home)
            db.session.commit()
        except:
            return make_response({'errors' : 'Apartment Not Found'}, 404)
        return make_response(new_home.to_dict(), 201)
    


api.add_resource(Apartments, '/apartments')

class ApartmentsById(Resource):

    def get(self, id):
        home = Apartment.query.filter_by(id = id).first().to_dict()
        return make_response(jsonify(home), 200)
    
    def patch(self, id):
        data = request.get_json()
        home = Apartment.query.filter_by(id = id).first()
        for attr in data:
            setattr(home, attr, data[attr])
            db.session.add(home)
            db.session.commit()
    
        home_dict = home.to_dict()
        response = make_response(home_dict, 200)
        return response

    def delete(self, id):
        doomed = Apartment.query.filter_by(id = id).first()
        db.session.delete(doomed)
        db.session.commit()

        response_dict = { "message": " "}
        response = make_response(response_dict, 204)
        return response
    

api.add_resource(ApartmentsById, '/apartments/<int:id>')

class Tenants(Resource):
    def get(self):
        peeps = Tenant.query.all()
        people_list = []
        for p in peeps:
            p_dict = {
                "id": p.id,
                "name": p.name,
                "age": p.age,
            }
            people_list.append(p_dict)
        return make_response(jsonify(people_list), 200)
    
    def post(self):
        data = request.get_json()
        try:
            new_ten = Tenant(
                name = data['name'],
                age = data['age']
            )
            db.session.add(new_ten)
            db.session.commit()
        except:
            return make_response({'errors' : 'Tenant Not Found'}, 404)
        return make_response(new_ten.to_dict(), 201)
    
api.add_resource(Tenants, '/tenants')

class TenantsById(Resource):

    def get(self, id):
        try:
            peeps = Tenant.query.filter_by(id = id).first().to_dict()
        except:
            return make_response(jsonify({"message": "tenant not found"}), 404)
        return make_response(jsonify(peeps), 200)
    
    def patch(self, id):
        data = request.get_json()
        person = Tenant.query.filter_by(id = id).first()
        for attr in data:
            setattr(person, attr, data[attr])
            db.session.add(person)
            db.session.commit()
    
        person_dict = person.to_dict()
        response = make_response(person_dict, 200)
        return response
    
    def delete(self, id):
        try:
            doomed = Tenant.query.filter_by(id = id).first()
        except:
            return make_response(jsonify({"message": "tenant not found"}), 404)
        
        db.session.delete(doomed)
        db.session.commit()

        response_dict = { "message": " "}
        response = make_response(response_dict, 204)
        return response

api.add_resource(TenantsById, '/tenants/<int:id>')

class LeasesById(Resource):

    def get(self, id):
        try:
            money = Lease.query.filter_by(id = id).first().to_dict()
        except:
            return make_response(jsonify({"message": "lease not found"}), 404)
        return make_response(jsonify(money), 200)
    
    def delete(self, id):
        
        try: 
            doomed = Lease.query.filter_by(id = id).first()
            
        except:
            return make_response(jsonify({"message": "lease not found"}), 404)
        
        db.session.delete(doomed)
        db.session.commit()

        response_dict = { "message": " "}
        response = make_response(response_dict, 204)
        return response

api.add_resource(LeasesById, '/leases/<int:id>')

if __name__ == '__main__':
    app.run( port = 3000, debug = True )