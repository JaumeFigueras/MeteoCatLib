#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..database import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Measure(db.Base):
    """
    Class container for measures table.  It provides SQL Alchemy access to the measures read from the weather stations
    """
    __tablename__ = 'meteocat_measure'
    id = Column(Integer, primary_key=True)
    date = Column('_data', DateTime(timezone=True), nullable=False)
    date_extreme_record = Column('_data_extrem', DateTime(timezone=True), nullable=False)
    value = Column('_valor', Float, nullable=False)
    status = Column('_estat', String, nullable=False)
    time_basis = Column('_base_horaria', String, nullable=False)
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='measures')
    variable = relationship('Variable', back_populates='measures')

    def __init__(self, date, value, status, time_basis, date_extreme_record=None):
        self.date = date
        self.date_extreme_record = date_extreme_record
        self.value = value
        self.status = status
        self.time_basis = time_basis
