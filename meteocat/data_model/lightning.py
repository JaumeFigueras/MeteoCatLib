#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import pytz
import json
import datetime
import dateutil.parser

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func
from geoalchemy2 import Geometry

from meteocat.data_model import Base

from typing import Union
from typing import Optional
from typing import Dict
from typing import Any


class Lightning(Base):
    """
    Class container for lightnings table.  It provides SQL Alchemy access to the registered lightnings. It also provides
    JSON coding and decoding

    :type id: int
    :type meteocat_id: int
    :type date: datetime.datetime
    :type peak_current: float
    :type chi_squared: float
    :type ellipse_major_axis: float
    :type ellipse_minor_axis: float
    :type ellipse_angle: float
    :type number_of_sensors: float
    :type hit_ground: float
    :type municipality_code: float
    :type _coordinates_latitude: float
    :type _coordinates_longitude: float
    :type ts: datetime.datetime
    :type geometry: str or None

    TODO Testing for custom SRID
    """
    __tablename__ = 'lightning'
    DEFAULT_SRID_LIGHTNINGS = 4258  # EPSG code for the used SRS in the locations
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    """Unique ID in the table for a lightning. Differs from the meteocat ID because it is used as a Feature id in 
    geospatial formats"""
    meteocat_id = mapped_column('_id', Integer, unique=True, nullable=False)
    date = mapped_column('_data', DateTime(timezone=True), nullable=False)
    peak_current = mapped_column('_corrent_pic', Float, nullable=False)
    chi_squared = mapped_column('_chi2', Float, default=None)
    ellipse_major_axis = mapped_column('_ellipse_eix_major', Float, nullable=False)
    ellipse_minor_axis = mapped_column('_ellipse_eix_menor', Float, nullable=False)
    ellipse_angle = mapped_column('_ellipse_angle', Float, nullable=False)
    number_of_sensors = mapped_column('_num_sensors', Integer, nullable=False)
    hit_ground = mapped_column('_nuvol_terra', Boolean, nullable=False)
    municipality_code = mapped_column('_id_municipi', Integer, default=None)
    _coordinates_latitude = mapped_column('_coordenades_latitud', Float, nullable=False)
    _coordinates_longitude = mapped_column('_coordenades_longitud', Float, nullable=False)
    ts = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    geometry = mapped_column('geom', Geometry(geometry_type='POINT', srid=DEFAULT_SRID_LIGHTNINGS))
    srid = None

    def __init__(self, meteocat_id: Optional[int] = None, date: Optional[Union[str, datetime.datetime]] = None,
                 peak_current: Optional[float] = None, chi_squared: Optional[float] = None,
                 ellipse_major_axis: Optional[float] = None, ellipse_minor_axis: Optional[float] = None,
                 ellipse_angle: Optional[float] = None, number_of_sensors: Optional[int] = None,
                 hit_ground: Optional[bool] = None, municipality_code: Optional[int] = None,
                 coordinates_latitude: Optional[float] = None, coordinates_longitude: Optional[float] = None) -> None:
        """
        Lightning constructor

        :param meteocat_id: Meteocat lightning ID
        :type meteocat_id: int
        :param date: Date and time when the lightning was recorded
        :type date: Union[datetime.datetime, str]
        :param peak_current: Peak current of the lightning
        :type peak_current: float
        :param chi_squared: Chi-square value of the lightning strike
        :type chi_squared: float
        :param ellipse_major_axis: Semi-major axis length value of the flash
        :type ellipse_major_axis: float
        :param ellipse_minor_axis: Semi-minor axis length value of the flash
        :type ellipse_minor_axis: float
        :param ellipse_angle: Ellipse angle (azimuth  from  the  north) value
        :type ellipse_angle: float
        :param number_of_sensors: N umber of detectors than have participated in the reading
        :type number_of_sensors: int
        :param hit_ground: It is a lightning that has hit the ground or a cloud-to-cloud lightning
        :type hit_ground: bool
        :param municipality_code: ID of the municipality where the strike has hit (optional)
        :type municipality_code: int
        :param coordinates_latitude: Latitude of the hit location (EPSG:4258)
        :type coordinates_latitude: float
        :param coordinates_longitude: Longitude of the hit location (EPSG:4258)
        :type coordinates_longitude: float
        """
        super().__init__()
        self.meteocat_id = meteocat_id
        if isinstance(date, str):
            self.date = dateutil.parser.isoparse(date)
        else:
            self.date = date
        self.peak_current = peak_current
        self.chi_squared = chi_squared
        self.ellipse_major_axis = ellipse_major_axis
        self.ellipse_minor_axis = ellipse_minor_axis
        self.ellipse_angle = ellipse_angle
        self.number_of_sensors = number_of_sensors
        self.hit_ground = hit_ground
        self.municipality_code = municipality_code
        self._coordinates_latitude = coordinates_latitude
        self._coordinates_longitude = coordinates_longitude
        self.__format_geom()
        self.srid = None

    def __format_geom(self) -> None:
        """
        Unique procedure to convert the member attributes coordinate_latitude and coordinate longitude to a OSGeo WKT
        standard format

        :return: None
        """
        if (self._coordinates_latitude is not None) and (self._coordinates_longitude is not None):
            self.geometry = "SRID={2:};POINT({0:} {1:})".format(self._coordinates_longitude, self._coordinates_latitude,
                                                                Lightning.DEFAULT_SRID_LIGHTNINGS)
        else:
            self.geometry = None

    @property
    def geom(self) -> str:
        """
        POSTGIS geometry text of the lightning location

        :return: Lightning location and SRS ID
        :rtype: str
        """
        return self.geometry

    @property
    def lat(self) -> float:
        """
        Latitude of the lightning location

        :return: Lightning latitude
        :rtype: float
        """
        return self._coordinates_latitude

    @lat.setter
    def lat(self, value: float) -> None:
        """
        Latitude setter. Value must be between -90 and 90 degrees

        :param value: Latitude value
        :type value: float
        :raise: ValueError
        :return: None
        """
        if -90 <= value <= 90:
            self._coordinates_latitude = value
            if self._coordinates_longitude is not None:
                self.__format_geom()
        else:
            raise ValueError("Latitude value must be between -90 and 90 degrees")

    @property
    def lon(self) -> float:
        """
        Longitude of the lightning location

        :return: Lightning longitude
        :rtype: float
        """
        return self._coordinates_longitude

    @lon.setter
    def lon(self, value: float) -> None:
        """
        Longitude setter. Value must be between -180 and 180 degrees

        :param value: Longitude value
        :type value: float
        :raise: ValueError
        :return: None
        """
        if -180 <= value <= 180:
            self._coordinates_longitude = value
            if self._coordinates_latitude is not None:
                self.__format_geom()
        else:
            raise ValueError("Longitude value must be between -180 and 180 degrees")

    @property
    def x(self) -> float:
        """
        Longitude of the lightning location

        :return: Lightning latitude
        :rtype: float
        """
        return self._coordinates_longitude

    @x.setter
    def x(self, value: float) -> None:
        """
        X setter.

        :param value: Latitude value
        :type value: float
        :raise: ValueError
        :return: None
        """
        self._coordinates_longitude = value

    @property
    def y(self) -> float:
        """
        Latitude of the lightning location

        :return: Lightning latitude
        :rtype: float
        """
        return self._coordinates_latitude

    @y.setter
    def y(self, value: float) -> None:
        """
        Y setter.

        :param value: Latitude value
        :type value: float
        :raise: ValueError
        :return: None
        """
        self._coordinates_latitude = value

    @staticmethod
    def object_hook_meteocat(dct: Dict[Any]) -> Union[Dict[Any], Lightning, None]:
        """
        Decodes a JSON originated dict from the Meteocat API to a Lightning object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict
        :return: Lightning
        """
        # Ellipse dict of the Meteocat API JSON
        if all(k in dct for k in ('eixMajor', 'eixMenor', 'angle')):
            return dct
        # Lat-lon coordinates dict of the Meteocat API JSON
        if all(k in dct for k in ('latitud', 'longitud')):
            return dct
        if not (all(k in dct for k in ('id', 'data', 'correntPic', 'chi2', 'ellipse', 'numSensors', 'nuvolTerra',
                                       'coordenades'))):
            return None
        lightning = Lightning()
        lightning.meteocat_id = int(dct['id'])
        try:
            lightning.date = dateutil.parser.isoparse(dct['data'])
        except ValueError:
            return None
        lightning.peak_current = float(dct['correntPic'])
        lightning.chi_squared = float(dct['chi2'])
        lightning.ellipse_major_axis = float(dct['ellipse']['eixMajor'])
        lightning.ellipse_minor_axis = float(dct['ellipse']['eixMenor'])
        lightning.ellipse_angle = float(dct['ellipse']['angle'])
        lightning.number_of_sensors = float(dct['numSensors'])
        lightning.hit_ground = bool(dct['nuvolTerra'])
        lightning._coordinates_latitude = float(dct['coordenades']['latitud'])
        lightning._coordinates_longitude = float(dct['coordenades']['longitud'])
        if 'idMunicipi' in dct:
            lightning.municipality_code = int(dct['idMunicipi'])
        else:
            lightning.municipality_code = None
        lightning.__format_geom()
        return lightning

    @staticmethod
    def object_hook_gisfire(dct: Dict[Any]) -> Union[Lightning, None]:
        """
        Decodes a JSON originated dict from the GisFIRE API to a Lightning object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict
        :return: Lightning
        """
        lightning = Lightning()
        lightning.id = int(dct['id'])
        lightning.meteocat_id = int(dct['meteocat_id'])
        try:
            lightning.date = dateutil.parser.isoparse(dct['date'])
        except ValueError:
            return None
        lightning.peak_current = float(dct['peak_current'])
        lightning.chi_squared = float(dct['chi_squared'])
        lightning.ellipse_major_axis = float(dct['ellipse_major_axis'])
        lightning.ellipse_minor_axis = float(dct['ellipse_minor_axis'])
        if dct['ellipse_angle'] is None:
            lightning.ellipse_angle = 0.0
        else:
            lightning.ellipse_angle = float(dct['ellipse_angle'])
        lightning.number_of_sensors = int(dct['number_of_sensors'])
        lightning.hit_ground = bool(dct['hit_ground'])
        if dct['municipality_code'] is not None:
            lightning.municipality_code = int(dct['municipality_code'])
        else:
            lightning.municipality_code = None
        lightning._coordinates_longitude = float(dct['coordinates_x']) if 'coordinates_x' in dct else (
            float(dct['coordinates_longitude']))
        lightning._coordinates_latitude = float(dct['coordinates_y']) if 'coordinates_y' in dct else (
            float(dct['coordinates_latitude']))
        lightning.srid = int(dct['coordinates_epsg'])
        lightning.__format_geom()
        return lightning

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a database lightning to JSON
        """

        def default(self, obj: Lightning) -> Union[Dict[str, Any], Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: Lightning
            :return: dict
            """
            if isinstance(obj, Lightning):
                dct = dict()
                dct['id'] = obj.id
                dct['meteocat_id'] = obj.meteocat_id
                dct['date'] = obj.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                dct['peak_current'] = obj.peak_current
                dct['chi_squared'] = obj.chi_squared
                dct['ellipse_major_axis'] = obj.ellipse_major_axis
                dct['ellipse_minor_axis'] = obj.ellipse_minor_axis
                dct['ellipse_angle'] = obj.ellipse_angle
                dct['number_of_sensors'] = obj.number_of_sensors
                dct['hit_ground'] = obj.hit_ground
                dct['municipality_code'] = obj.municipality_code
                if obj.srid is None or obj.srid == Lightning.DEFAULT_SRID_LIGHTNINGS:
                    dct['coordinates_latitude'] = obj._coordinates_latitude
                    dct['coordinates_longitude'] = obj._coordinates_longitude
                    dct['coordinates_epsg'] = Lightning.DEFAULT_SRID_LIGHTNINGS
                else:
                    dct['coordinates_y'] = obj._coordinates_latitude
                    dct['coordinates_x'] = obj._coordinates_longitude
                    dct['coordinates_epsg'] = obj.srid
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover

    class GeoJSONEncoder(json.JSONEncoder):
        """
        Geo JSON Encoder to convert a database lightning to JSON
        """

        def default(self, obj: Lightning) -> Union[Dict[str, Any], Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: Lightning
            :return: dict
            """
            if isinstance(obj, Lightning):
                dct = dict()
                dct['type'] = 'Feature'
                dct['id'] = obj.id
                dct['geometry'] = dict()
                dct['geometry']['type'] = 'Point'
                dct['geometry']['coordinates'] = [obj._coordinates_longitude, obj._coordinates_latitude]
                dct['crs'] = dict()
                dct['crs']['type'] = 'link'
                dct['crs']['properties'] = dict()
                if obj.srid is None or obj.srid == Lightning.DEFAULT_SRID_LIGHTNINGS:
                    dct['crs']['properties']['href'] = 'https://spatialreference.org/ref/epsg/' + \
                                                       str(Lightning.DEFAULT_SRID_LIGHTNINGS) + '/proj4/'
                else:
                    dct['crs']['properties']['href'] = 'https://spatialreference.org/ref/epsg/' + \
                                                       str(obj.srid) + '/proj4/'
                dct['crs']['properties']['type'] = 'proj4'
                dct['properties'] = dict()
                dct['properties']['id'] = obj.id
                dct['properties']['meteocat_id'] = obj.meteocat_id
                dct['properties']['date'] = obj.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                dct['properties']['peak_current'] = obj.peak_current
                dct['properties']['chi_squared'] = obj.chi_squared
                dct['properties']['ellipse_major_axis'] = obj.ellipse_major_axis
                dct['properties']['ellipse_minor_axis'] = obj.ellipse_minor_axis
                dct['properties']['ellipse_angle'] = obj.ellipse_angle
                dct['properties']['number_of_sensors'] = obj.number_of_sensors
                dct['properties']['hit_ground'] = obj.hit_ground
                dct['properties']['municipality_code'] = obj.municipality_code
                if obj.srid is None or obj.srid == Lightning.DEFAULT_SRID_LIGHTNINGS:
                    dct['properties']['coordinates_latitude'] = obj._coordinates_latitude
                    dct['properties']['coordinates_longitude'] = obj._coordinates_longitude
                    dct['properties']['coordinates_epsg'] = Lightning.DEFAULT_SRID_LIGHTNINGS
                else:
                    dct['properties']['coordinates_y'] = obj._coordinates_latitude
                    dct['properties']['coordinates_x'] = obj._coordinates_longitude
                    dct['properties']['coordinates_epsg'] = obj.srid
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover


class LightningAPIRequest(Base):
    """
    Class container for the lightnings requests table.  It provides SQL Alchemy access to the performed requests to the
    remote API. As data is event driven it is not possible to know if there were lightnings at a certain time

    :type date: datetime.datetime
    :type http_status_code: int
    :type number_of_lightnings: int
    :type ts: datetime.datetime
    """
    __tablename__ = 'xdde_request'
    date = Column('request_date', DateTime(timezone=True), primary_key=True)
    http_status_code = Column(Integer, nullable=False, default=200)
    number_of_lightnings = Column(Integer, nullable=True, default=None)
    ts = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __init__(self, date: Union[str, datetime.datetime, None] = None, http_status_code: Union[int, None] = None,
                 number_of_lightnings: Union[int, None] = None):
        """
        Lightning API Request Constructor

        :param date: Date of the request if it is passed as string must be ISO compliant. Minutes and seconds will be
        truncated to 0 each
        :type date: Union[datetime.date, str]
        :param http_status_code: HTTP status code of the request
        :type http_status_code: int
        :param number_of_lightnings: Number of lightnings obtained from the Meteocat API call
        :type number_of_lightnings: int
        """
        super().__init__()
        if type(date) is str:
            self.date = dateutil.parser.isoparse(date).replace(minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)
        else:
            self.date = date.replace(minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)
        self.http_status_code = http_status_code
        self.number_of_lightnings = number_of_lightnings
