#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class WeatherStationVariableTimeBasisAssociation(Base):
    """
    Class container for the association table between weather stations, variables and the time basis of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'meteocat_station_variable_time_association'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_time_basis_id = Column(Integer, ForeignKey('meteocat_variable_time_basis.id'), primary_key=True)
    station = relationship('WeatherStation', backref='time_basis')
    variable = relationship('Variable', backref='time_basis')
    time_basis = relationship('VariableTimeBasis', backref='time_basis')


class WeatherStationVariableStatusAssociation(Base):
    """
    Class container for the association table between weather stations, variables and the status of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'meteocat_station_variable_status_association'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_status_id = Column(Integer, ForeignKey('meteocat_variable_status.id'), primary_key=True)
    station = relationship('WeatherStation', backref='variable_status', foreign_keys=[meteocat_weather_station_id])
    variable = relationship('Variable', backref='variable_status', foreign_keys=[meteocat_variable_id])
    status = relationship('VariableStatus', backref='variable_status', foreign_keys=[meteocat_variable_status_id])


