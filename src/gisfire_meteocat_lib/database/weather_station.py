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
from sqlalchemy import Table
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship

SRID_WEATHER_STATIONS = 4258


class WeatherStationStatus(db.Base):
    __tablename__ = 'meteocat_weather_station_status'
    id = Column(Integer, primary_key=True)
    _codi = Column(Integer, nullable=False)
    _data_inici = Column(DateTime(timezone=True), nullable=False)
    _data_fi = Column(DateTime(timezone=True))
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='status')

    def __init__(self, _codi, _data_inici, _data_fi=None):
        self._codi = _codi
        self._data_inici = _data_inici
        self._data_fi = _data_fi


weather_station_variable_status_association_table = \
    Table('meteocat_station_variable_status_association', db.Base.metadata,
          Column('meteocat_weather_station_id', ForeignKey('meteocat_weather_station.id'), primary_key=True),
          Column('meteocat_variable_id', ForeignKey('meteocat_variable.id'), primary_key=True),
          Column('meteocat_variable_status_id', ForeignKey('meteocat_variable_status.id'), primary_key=True))


class WeatherStation(db.Base):
    __tablename__ = 'meteocat_weather_station'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False, unique=True)
    _nom = Column(String, nullable=False)
    _tipus = Column(String, nullable=False)
    _coordenades_latitud = Column(Float, nullable=False)
    _coordenades_longitud = Column(Float, nullable=False)
    _emplacament = Column(String, nullable=False)
    _altitud = Column(Float, nullable=False)
    _municipi_codi = Column(Integer, nullable=False)
    _municipi_nom = Column(String, nullable=False)
    _comarca_codi = Column(Integer, nullable=False)
    _comarca_nom = Column(String, nullable=False)
    _provincia_codi = Column(Integer, nullable=False)
    _provincia_nom = Column(String, nullable=False)
    _xarxa_codi = Column(Integer, nullable=False)
    _xarxa_nom = Column(String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    geom = Column(Geometry(geometry_type='POINT', srid=SRID_WEATHER_STATIONS))
    status = relationship("WeatherStationStatus", back_populates='station', lazy='joined')
    measures = relationship("Measure", back_populates='station', lazy='select')
    variables = relationship("Variable", secondary=weather_station_variable_status_association_table,
                             back_populates="stations", lazy='select')
    variables_status = relationship("VariableStatus", secondary=weather_station_variable_status_association_table,
                                    back_populates="stations", lazy='select')

    def __init__(self, codi, nom, tipus, coordenades_latitud, coordenades_longitud, emplacament, altitud,
                 municipi_codi, municipi_nom, comarca_codi, comarca_nom, provincia_codi, provincia_nom,
                 xarxa_codi, xarxa_nom):
        self._codi = codi
        self._nom = nom
        self._tipus = tipus
        self._coordenades_latitud = coordenades_latitud
        self._coordenades_longitud = coordenades_longitud
        self._emplacament = emplacament
        self._altitud = altitud
        self._municipi_codi = municipi_codi
        self._municipi_nom = municipi_nom
        self._comarca_codi = comarca_codi
        self._comarca_nom = comarca_nom
        self._provincia_codi = provincia_codi
        self._provincia_nom = provincia_nom
        self._xarxa_codi = xarxa_codi
        self._xarxa_nom = xarxa_nom
        self.geom = "SRID={2:};POINT({0:} {1:})".format(self._coordenades_longitud, self._coordenades_latitud,
                                                        SRID_WEATHER_STATIONS)

    @property
    def code(self):
        return self.__codi

    @code.setter
    def code(self, code):
        self._codi = code

