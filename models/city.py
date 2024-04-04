#/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
        Class: City.

        Info: The city class

        Attributes:
            __tablename__ (str): The name of the MySQL
            name (sqlalchemy String): The name
            state_id (sqlalchemy String): The state id
     """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities', cascade='delete')
