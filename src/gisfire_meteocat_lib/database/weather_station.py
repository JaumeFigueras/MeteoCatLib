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
    STATUS_DISMANTLED = 1
    STATUS_ACTIVE = 2
    STATUS_REPAIR = 3
    SRID_WEATHER_STATIONS = 4258
    __tablename__ = 'meteocat_weather_station'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False, unique=True)
    name = Column('_nom', String, nullable=False)
    category = Column('_tipus', String, nullable=False)
    coordinates_latitude = Column('_coordenades_latitud', Float, nullable=False)
    coordinates_longitude = Column('_coordenades_longitud', Float, nullable=False)
    placement = Column('_emplacament', String, nullable=False)
    altitude = Column('_altitud', Float, nullable=False)
    municipality_code = Column('_municipi_codi', Integer, nullable=False)
    municipality_name = Column('_municipi_nom', String, nullable=False)
    county_code = Column('_comarca_codi', Integer, nullable=False)
    county_name = Column('_comarca_nom', String, nullable=False)
    province_code = Column('_provincia_codi', Integer, nullable=False)
    province_name = Column('_provincia_nom', String, nullable=False)
    network_code = Column('_xarxa_codi', Integer, nullable=False)
    network_name = Column('_xarxa_nom', String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    geom = Column(Geometry(geometry_type='POINT', srid=SRID_WEATHER_STATIONS))
    status = relationship("WeatherStationStatus", back_populates='station', lazy='joined')
    measures = relationship("Measure", back_populates='station', lazy='select')

    def __init__(self, code, name, category, coordinates_latitude, coordinates_longitude, placement, altitude,
                 municipality_code, municipality_name, county_code, county_name, province_code, province_name,
                 network_code, network_name):
        self.code = code
        self.name = name
        self.category = category
        self.coordinates_latitude = coordinates_latitude
        self.coordinates_longitude = coordinates_longitude
        self.placement = placement
        self.altitude = altitude
        self.municipality_code = municipality_code
        self.municipality_name = municipality_name
        self.county_code = county_code
        self.county_name = county_name
        self.province_code = province_code
        self.province_name = province_name
        self.network_code = network_code
        self.network_name = network_name
        self.geom = "SRID={2:};POINT({0:} {1:})".format(self.coordinates_longitude, self.coordinates_latitude,
                                                        self.SRID_WEATHER_STATIONS)


