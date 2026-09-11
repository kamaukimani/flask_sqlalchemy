from app.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .item import Item
from .customer import Customer
from sqlalchemy_serializer import SerializerMixin

class Review(db.Model,SerializerMixin):
    __tablename__="reviews"

    serialize_rules=("-customer.reviews","-item.reviews",)

    id:Mapped[int]=mapped_column(primary_key=True)
    comment:Mapped[str]
    
    customer_id:Mapped[int]=mapped_column(ForeignKey("customers.id"))
    item_id:Mapped[int]=mapped_column(ForeignKey("items.id"))

    customer:Mapped["Customer"]=relationship(back_populates="reviews")
    item:Mapped["Item"]=relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review {self.id}: {self.comment}>"