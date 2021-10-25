#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class VariableStatus(db.Base):
    __tablename__ = 'meteocat_variable_status'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', Integer, nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, code, from_date, to_date=None):
        self.code = code
        self.from_date = from_date
        self.to_date = to_date


class Variable(db.Base):
    __tablename__ = 'meteocat_variable'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False, unique=True)
    name = Column('_nom', String, nullable=False)
    unit = Column('_unitat', String, nullable=False)
    acronym = Column('_acronim', String, nullable=False)
    category = Column('_tipus', String, nullable=False)
    decimals = Column('_decimals', String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    measures = relationship('Measure', back_populates='variable')

    def __init__(self, code, name, unit, acronym, category, decimals):
        self.code = code
        self.name = name
        self.unit = unit
        self.acronym = acronym
        self.category = category
        self.decimals = decimals


class WeatherStationVariableTimeBasisAssociation(db.Base):
    __tablename__ = 'meteocat_station_variable_time_association'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_time_basis_id = Column(Integer, ForeignKey('meteocat_variable_time_basis.id'), primary_key=True)
    station = relationship('WeatherStation', backref='time_basis')
    variable = relationship('Variable', backref='time_basis')
    time_basis = relationship('VariableTimeBasis', backref='time_basis')


class VariableTimeBasis(db.Base):
    __tablename__ = 'meteocat_variable_time_basis'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, code, from_date, to_date=None):
        self.code = code
        self.from_date = from_date
        self.to_date = to_date


