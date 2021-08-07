from sqlalchemy import Column, Text, SmallInteger
from sqlalchemy.sql.sqltypes import Float
from database.connection import Base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from schemas.restaurant_schema import NotFoundRestaurantException


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

    @classmethod
    def find(cls, id, db):
        try:
            row = db.query(cls).filter(cls.id == id)
            if not row.first():
                raise NotFoundRestaurantException(id)

            return row
        except:
            raise NotFoundRestaurantException(id)

    def dict(self):
        dic = self.__dict__
        dic['id'] = str(self.id)
        del dic['_sa_instance_state']

        return dic
