# Creation of a declarative base for the SQL Alchemy models to inherit from
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Imports needed by SQL Alchemy to process the relations correctly
from .weather_station import *  # noqa: E402
from .variable import *  # noqa: E402
from .measure import *  # noqa: E402
from .relations import *  # noqa: E402
