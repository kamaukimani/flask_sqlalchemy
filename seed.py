#!/usr/bin/env python3

from app import create_app
from app.db import db
from app.models import *
# from app.models.customer import Customer
# from app.models.item import Item
# from app.models.review import Review

app=create_app()

with app.app_context():

    # Review.query.delete()
    # Customer.query.delete()
    
    # Item.query.delete()

    # customer1 = Customer(name='Tal Yuri')
    # customer2 = Customer(name='Raha Rosario')
    # customer3 = Customer(name='Luca Mahan')
    # db.session.add_all([customer1, customer2, customer3])
    # db.session.commit()

    # item1 = Item(name='Laptop Backpack', price=49.99)
    # item2 = Item(name='Insulated Coffee Mug', price=9.99)
    # item3 = Item(name='6 Foot HDMI Cable', price=12.99)
    # db.session.add_all([item1, item2, item3])
    # db.session.commit()

    # db.session.add(Review(comment="zipper broke the first week",
    #                customer=customer1, item=item1))
    # db.session.add(Review(comment="love this backpack!",
    #                customer=customer2, item=item1))
    # db.session.add(Review(comment="coffee stays hot for hours!",
    #                customer=customer1, item=item2))
    # db.session.add(Review(comment="best coffee mug ever!",
    #                customer=customer3, item=item2))
    # db.session.add(Review(comment="cable too short",
    #                customer=customer3, item=item3))
    # db.session.commit()

    customer1=Customer.query.filter_by(id=1).first()
    print(customer1)
    print(f"customer 1 items:{customer1.items}")