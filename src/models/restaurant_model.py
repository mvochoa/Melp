from sqlalchemy import Column, Text, SmallInteger
from sqlalchemy.sql.sqltypes import Float
from database.connection import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class RestaurantModel(Base):
    __tablename__ = 'restaurants'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    rating = Column(SmallInteger)
    name = Column(Text)
    site = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    street = Column(Text)
    city = Column(Text)
    state = Column(Text)
    lat = Column(Float)
    lng = Column(Float)
