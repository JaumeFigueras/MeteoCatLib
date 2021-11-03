#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ..database import db
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func
from geoalchemy2 import Geometry


class Lightning(db.Base):
    """
    Class container for lightnings table.  It provides SQL Alchemy access to the registered lightnings
    """
    __tablename__ = 'meteocat_lightning'
    SRID_LIGHTNINGS = 4258
    id = Column(Integer, primary_key=True)
    meteocat_id = Column('_id', Integer, unique=True, nullable=False)
    date = Column('_data', DateTime(timezone=True), nullable=False)
    peak_current = Column('_corrent_pic', Float, nullable=False)
    chi_squared = Column('_chi2', Float, nullable=False)
    ellipse_major_axis = Column('_ellipse_eix_major', Float, nullable=False)
    ellipse_minor_axis = Column('_ellipse_eix_menor', Float, nullable=False)
    ellipse_angle = Column('_ellipse_angle', Float, nullable=False)
    number_of_sensors = Column('_num_sensors', Integer, nullable=False)
    hit_ground = Column('_nuvol_terra', Boolean, nullable=False)
    municipality_code = Column('_id_municipi', Integer, nullable=False)
    coordinates_latitude = Column('_coordenades_latitud', Float, nullable=False)
    coordinates_longitude = Column('_coordenades_longitud', Float, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    geom = Column(Geometry(geometry_type='POINT', srid=SRID_LIGHTNINGS))

    def __init__(self, meteocat_id, date, peak_current, chi_squared, ellipse_major_axis, ellipse_minor_axis,
                 ellipse_angle, number_of_sensors, hit_ground, municipality_code, coordinates_latitude,
                 coordinates_longitude):
        self.meteocat_id = meteocat_id
        self.date = date
        self.peak_current = peak_current
        self.chi_squared = chi_squared
        self.ellipse_major_axis = ellipse_major_axis
        self.ellipse_minor_axis = ellipse_minor_axis
        self.ellipse_angle = ellipse_angle
        self.number_of_sensors = number_of_sensors
        self.hit_ground = hit_ground
        self.municipality_code = municipality_code
        self.coordinates_latitude = coordinates_latitude
        self.coordinates_longitude = coordinates_longitude
        self.geom = "SRID={2:};POINT({0:} {1:})".format(self.coordinates_longitude, self.coordinates_latitude,
                                                        self.SRID_LIGHTNINGS)


class LightningAPIRequest(db.Base):
    """
    Class container for the lightnings requests table.  It provides SQL Alchemy access to the performed requests to the
    remote API. As data is event driven it is not possible to know if there were lightnings at a certain time
    """
    __tablename__ = 'meteocat_xdde_request'
    year = Column(Integer, primary_key=True)
    month = Column(Integer, primary_key=True)
    day = Column(Integer, primary_key=True)
    hour = Column(Integer, primary_key=True)
    result_code = Column(Integer, nullable=False, default=200)
    number_of_lightnings = Column(Integer, nullable=True, default=None)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, year, month, day, hour, result_code, number_of_lightnings):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.result_code = result_code
        self.number_of_lightnings = number_of_lightnings
