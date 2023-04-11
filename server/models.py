from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

#  Tenant --> Lease <--Apartments

class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    serialize_rules = ('-tenant.leases' ,)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Tenant must have a Name")
        return value
    
    apartments = association_proxy('lease', 'apartment', creator=lambda ap:Lease(apartment=ap))
    leases = db.relationship("Lease", backref='tenant')
    
class Apartment(db.Model, SerializerMixin):
    __tablename__ = 'apartments'

    serialize_rules = ('-apartment.leases', )

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    tenants = association_proxy('lease', 'tenant', creator=lambda tn:Lease(tenant=tn))
    leases = db.relationship("Lease", backref='apartment')

class Lease(db.Model, SerializerMixin):
    __tablename__ = 'leases'

    serialize_rules = ('-apartment.leases', '-tenant.leases', )

    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
