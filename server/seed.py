#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

with app.app_context():
    # Create the tables in the database
    db.create_all()

    # Optional: clear old data
    Pet.query.delete()

    # Add some Pet instances
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster")
    ]

    db.session.add_all(pets)
    db.session.commit()

    print("Seeded pets!")
