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
    __tablename__ = 'meteocat_weather_stations_status'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False)
    _data_inici = Column(DateTime(timezone=True), nullable=False)
    _data_fi = Column(DateTime(timezone=True))
    meteocat_weather_stations_id = Column(Integer, ForeignKey('meteocat_weather_stations.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, _codi, _data_inici, _data_fi=None):
        self._codi = _codi
        self._data_inici = _data_inici
        self._data_fi = _data_fi


class WeatherStation(db.Base):
    __tablename__ = 'meteocat_weather_stations'
    id = Column(Integer, primary_key=True)
    _codi = Column(String, nullable=False, unique=True)
    _nom = Column(String, nullable=False)
    _tipus = Column(String, nullable=False)
    _coordenades_latitud = Column(Float, nullable=False)
    _coordenades_longitud = Column(Float, nullable=False)
    _emplacament  = Column(String, nullable=False)
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
    status = relationship("WeatherStationStatus", backref='meteocat_weather_stations')

    def __init__(self, _codi, _nom, _tipus, _coordenades_latitud, _coordenades_longitud, _emplacament, _altitud,
                 _municipi_codi, _municipi_nom, _comarca_codi, _comarca_nom, _provincia_codi, _provincia_nom,
                 _xarxa_codi, _xarxa_nom):
        self._codi = _codi
        self._nom = _nom
        self._tipus = _tipus
        self._coordenades_latitud = _coordenades_latitud
        self._coordenades_longitud = _coordenades_longitud
        self._emplacament = _emplacament
        self._altitud = _altitud
        self._municipi_codi = _municipi_codi
        self._municipi_nom = _municipi_nom
        self._comarca_codi = _comarca_codi
        self._comarca_nom = _comarca_nom
        self._provincia_codi = _provincia_codi
        self._provincia_nom = _provincia_nom
        self._xarxa_codi = _xarxa_codi
        self._xarxa_nom = _xarxa_nom
        self.geom = "SRID={2:};POINT({0:} {1:})".format(self._coordenades_longitud, self._coordenades_latitud,
                                                        SRID_WEATHER_STATIONS)
