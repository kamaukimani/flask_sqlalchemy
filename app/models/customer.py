from app.db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Customer(db.Model):
    __tablename__="customers"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]

    reviews:Mapped[List["Review"]]=relationship(back_populates="customer",cascade="all,delete-orphan")
    items=association_proxy("reviews","item",creator=lambda item_obj:Review(item=item_obj))

    def __repr__(self):
        return f"<Customer {self.id}: {self.name}>"