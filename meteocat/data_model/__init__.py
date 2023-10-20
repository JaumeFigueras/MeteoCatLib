#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Creation of a declarative base for the SQL Alchemy models to inherit from
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Imports needed by SQL Alchemy to process the relations correctly
from meteocat.data_model.lightning import *  # noqa: E402
from meteocat.data_model.relations import *  # noqa: E402
from meteocat.data_model.weather_station import *  # noqa: E402
from meteocat.data_model.variable import *  # noqa: E402
from meteocat.data_model.measure import *  # noqa: E402
