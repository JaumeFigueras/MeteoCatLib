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
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship

SRID_WEATHER_STATIONS = 4258


class WeatherStationStatus(db.Base):
    __tablename__ = 'meteocat_weather_station_status'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', Integer, nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='status')

    def __init__(self, code, from_date, to_date=None):
        self.code = code
        self.from_date = from_date
        self.to_date = to_date


class WeatherStationVariableStatusAssociation(db.Base):
    __tablename__ = 'meteocat_station_variable_status_association'
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'), primary_key=True)
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'), primary_key=True)
    meteocat_variable_status_id = Column(Integer, ForeignKey('meteocat_variable_status.id'), primary_key=True)
    station = relationship('WeatherStation', backref='variable_status')
    variable = relationship('Variable', backref='variable_status')
    status = relationship('VariableStatus', backref='variable_status')


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
    STATUS_DISMANTLED = 1
    STATUS_ACTIVE = 2
    STATUS_REPAIR = 3

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
        return self._codi

    @code.setter
    def code(self, code):
        self._codi = code

