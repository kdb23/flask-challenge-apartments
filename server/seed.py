from random import choice as rc, randint

from faker import Faker

from app import app
from models import db, Apartment, Lease, Tenant

fake = Faker()

def make_tenant():

    Tenant.query.delete()

    tenants = []

    for i in range(50):
        tenant = Tenant(
            name=fake.name(),
            age=randint(18,100),
        )
        tenants.append(tenant)

    db.session.add_all(tenants)
    db.session.commit()

def make_apartments():

    Apartment.query.delete()

    apartments = []

    for i in range(100):
        apartment = Apartment(
            number=randint(1000,2000),
        )
        apartments.append(apartment)

    db.session.add_all(apartments)
    db.session.commit()

def make_lease():

    Lease.query.delete()
    tenants = Tenant.query.with_entities(Tenant.id).all()
    apartments = Apartment.query.with_entities(Apartment.id).all()
    print(tenants)
    print(apartments)

    leases = []

    for i in range(20):
        lease = Lease(
            rent=randint(1,100),
            tenant_id=rc(tenants)[0],
            apartment_id=rc(apartments)[0]
        )
        leases.append(lease)
    
    db.session.add_all(leases)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        make_lease()
        make_apartments()
        make_tenant()

    