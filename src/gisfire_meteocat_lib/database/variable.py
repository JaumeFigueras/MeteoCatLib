#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import db
from .weather_station import weather_station_variable_status_association_table
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
    _codi = Column(Integer, nullable=False)
    _data_inici = Column(DateTime(timezone=True), nullable=False)
    _data_fi = Column(DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    stations = relationship('WeatherStation', secondary=weather_station_variable_status_association_table,
                            back_populates='variables_status', lazy='select')
    variables = relationship('Variable', secondary=weather_station_variable_status_association_table,
                             back_populates='status', lazy='select')

    def __init__(self, _codi, _data_inici, _data_fi=None):
        self._codi = _codi
        self._data_inici = _data_inici
        self._data_fi = _data_fi


class Variable(db.Base):
    __tablename__ = 'meteocat_variable'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False, unique=True)
    _nom = Column(String, nullable=False)
    _unitat = Column(String, nullable=False)
    _acronim = Column(String, nullable=False)
    _tipus = Column(String, nullable=False)
    _decimals = Column(String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    measures = relationship('Measure', back_populates='variable')
    stations = relationship("WeatherStation", secondary=weather_station_variable_status_association_table,
                            back_populates='variables', lazy='select')
    status = relationship("VariableStatus", secondary=weather_station_variable_status_association_table,
                          back_populates='variables', lazy='select')

    def __init__(self, _codi, _nom, _unitat, _acronim, _tipus, _decimals):
        self._codi = _codi
        self._nom = _nom
        self._unitat = _unitat
        self._acronim = _acronim
        self._tipus = _tipus
        self._decimals = _decimals


