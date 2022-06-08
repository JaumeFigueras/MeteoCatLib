#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class WeatherStationVariableStateAssociation(Base):
    """
    Class container for the association table between weather stations, variables and the state of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'meteocat_station_variable_state_assoc'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_state_id = Column(Integer, ForeignKey('meteocat_variable_state.id'), primary_key=True)
    station = relationship('WeatherStation', backref='assoc_variable_state', foreign_keys=[meteocat_weather_station_id])
    variable = relationship('Variable', backref='assoc_variable_state', foreign_keys=[meteocat_variable_id])
    state = relationship('VariableState', backref='assoc_variable_state', foreign_keys=[meteocat_variable_state_id])


class WeatherStationVariableTimeBaseAssociation(Base):
    """
    Class container for the association table between weather stations, variables and the time basis of the variable.
    Provides the SQL Alchemy access to the ternary relation
    """
    __tablename__ = 'meteocat_station_variable_time_assoc'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_time_base_id = Column(Integer, ForeignKey('meteocat_variable_time_base.id'), primary_key=True)
    station = relationship('WeatherStation', backref='assoc_variable_time_base',
                           foreign_keys=[meteocat_weather_station_id])
    variable = relationship('Variable', backref='assoc_variable_time_base', foreign_keys=[meteocat_variable_id])
    time_base = relationship('VariableTimeBase', backref='assoc_variable_time_base',
                             foreign_keys=[meteocat_variable_time_base_id])
