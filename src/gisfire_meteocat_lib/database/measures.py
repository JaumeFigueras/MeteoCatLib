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
    __tablename__ = 'meteocat_measure'
    id = Column(Integer, primary_key=True)
    _data = Column(DateTime(timezone=True), nullable=False)
    _valor = Column(Float, nullable=False)
    _estat = Column(String, nullable=False)
    _base_horaria = Column(String, nullable=False)
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='measures')
    variable = relationship('Variable', back_populates='measures')

    def __init__(self, _data, _valor, _estat, _base_horaria):
        self._data = _data
        self._valor = _valor
        self._estat = _estat
        self._base_horaria = _base_horaria
