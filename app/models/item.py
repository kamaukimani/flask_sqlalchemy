from app.db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy

class Item(db.Model):
    __tablename__="items"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    price:Mapped[float]

    reviews:Mapped[List["Review"]]=relationship(back_populates="item",cascade="all,delete-orphan")
    customers=association_proxy("reviews","customer",creator=lambda customer_obj:Review(customer=customer_obj))


    def __repr__(self):
        return f"<Item {self.id}: {self.name}, {self.price}>"