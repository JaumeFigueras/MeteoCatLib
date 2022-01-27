# Creation of a declarative base for the SQL Alchemy models to inherit from
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Imports needed by SQL Alchemy to process the relations correctly
from .weather_station import *
from .variable import *
from .measure import *
from .relations import *

