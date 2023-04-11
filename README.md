# Flask Practice Challenge - Apartments

## Setup

To download the dependencies for backend, run:

```console
$ pipenv install
```

You can run your Flask API on [`localhost:3000`](http://localhost:3000) by entering the development environment with `pipenv shell`, then after changing into the `server` directory running:

```console
$ python app.py
```

There are no tests for this application, so you'll need to check your progress
by running the server and using Postman or JavaScript `fetch` to make requests.

## Introduction

We're going to build an API for an apartment management company. Create the
following database structure. You will have three models (and their
corresponding tables), `Apartment`, `Tenant` and `Lease`, with the following
relationships:

- A tenant has many apartments and has many leases
- An apartment has many tenants and has many leases
- A lease belongs to an apartment and belongs to a tenant

The models should have the following attributes (along with any attributes
needed to create the relationships defined above):

- Apartment
  - number
- Tenant
  - name (must be present)
  - age (must be >= 18)
- Lease
  - rent

Make sure to define validations for your models so that no bad data can be saved
to the database.

## Deliverables

As a user, I can:

- Create, read, update and delete **Apartments** (GET, POST, PATCH, DELETE)
- Create, read, update and delete **Tenants** (GET,POST,PATCH, DELETE)
- Create and delete **Lease** (GET & DELETE)

Follow good API design practices and use RESTful routing conventions. Make sure
to handle errors and invalid data by returning the appropriate status code along
with a message.

## Instructions

- Time yourself while working on the deliverables
- Commit when you hit 75 minutes
- When you have finished all deliverables, commit again.
