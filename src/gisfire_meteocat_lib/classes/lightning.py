#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func
from geoalchemy2 import Geometry
import dateutil.parser
import pytz
import json


class Lightning(Base):
    """
    Class container for lightnings table.  It provides SQL Alchemy access to the registered lightnings. It also provides
    JSON coding and decoding

    :type date: datetime.datetime
    """
    __tablename__ = 'meteocat_lightning'
    SRID_LIGHTNINGS = 4258
    id = Column(Integer, primary_key=True)
    meteocat_id = Column('_id', Integer, unique=True, nullable=False)
    date = Column('_data', DateTime(timezone=True), nullable=False)
    peak_current = Column('_corrent_pic', Float, nullable=False)
    chi_squared = Column('_chi2', Float, default=None)
    ellipse_major_axis = Column('_ellipse_eix_major', Float, nullable=False)
    ellipse_minor_axis = Column('_ellipse_eix_menor', Float, nullable=False)
    ellipse_angle = Column('_ellipse_angle', Float, nullable=False)
    number_of_sensors = Column('_num_sensors', Integer, nullable=False)
    hit_ground = Column('_nuvol_terra', Boolean, nullable=False)
    municipality_code = Column('_id_municipi', Integer, default=None)
    _coordinates_latitude = Column('_coordenades_latitud', Float, nullable=False)
    _coordinates_longitude = Column('_coordenades_longitud', Float, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    __geom = Column('geom', Geometry(geometry_type='POINT', srid=SRID_LIGHTNINGS))

    def __init__(self, meteocat_id=None, date=None, peak_current=None, chi_squared=None, ellipse_major_axis=None,
                 ellipse_minor_axis=None, ellipse_angle=None, number_of_sensors=None, hit_ground=None,
                 municipality_code=None, coordinates_latitude=None, coordinates_longitude=None):
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
        self.meteocat_id = meteocat_id
        if type(date) is str:
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

    def __format_geom(self):
        """
        Unique procedure to convert the member attributes coordinate_latitude and coordinate longitude to a OSGeo WKT
        standard format

        :return: None
        """
        if (self._coordinates_latitude is not None) and (self._coordinates_longitude is not None):
            self.__geom = "SRID={2:};POINT({0:} {1:})".format(self._coordinates_longitude, self._coordinates_latitude,
                                                              self.SRID_LIGHTNINGS)
        else:
            self.__geom = None

    @property
    def geom(self):
        """
        Latitude getter

        :return: Lightning latitude
        :rtype: float
        """
        return self.__geom

    @property
    def lat(self):
        """
        Latitude getter

        :return: Lightning latitude
        :rtype: float
        """
        return self._coordinates_latitude

    @lat.setter
    def lat(self, value):
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
    def lon(self):
        """
        Longitude getter

        :return: Lightning longitude
        :rtype: float
        """
        return self._coordinates_longitude

    @lon.setter
    def lon(self, value):
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

    @staticmethod
    def object_hook(dct):
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
        lightning.meteocat_id = dct['id']
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
        # lightning.__geom = "SRID={2:};POINT({0:} {1:})".format(lightning._coordinates_longitude,
        #                                                       lightning._coordinates_latitude,
        #                                                       Lightning.SRID_LIGHTNINGS)
        return lightning

    class JSONEncoder(json.JSONEncoder):
        """
        TODO:
        """

        def default(self, obj):
            """
            TODO:

            :param obj:
            :type obj: Lightning
            :return:
            """
            if isinstance(obj, Lightning):
                dct = dict()
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
                dct['coordinates_latitude'] = obj._coordinates_latitude
                dct['coordinates_longitude'] = obj._coordinates_longitude
                dct['coordinates_epsg'] = Lightning.SRID_LIGHTNINGS
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover


class LightningAPIRequest(Base):
    """
    Class container for the lightnings requests table.  It provides SQL Alchemy access to the performed requests to the
    remote API. As data is event driven it is not possible to know if there were lightnings at a certain time
    """
    __tablename__ = 'meteocat_xdde_request'
    date = Column('request_date', DateTime(timezone=True), primary_key=True)
    http_status_code = Column(Integer, nullable=False, default=200)
    number_of_lightnings = Column(Integer, nullable=True, default=None)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, date=None, http_status_code=None, number_of_lightnings=None):
        """
        Lightning API Request Constructor

        :param date: Date of the request if it is passed as string must be ISO compliant. Minutes and seconds will be
        truncated to 0 each
        :type date: Union[datetime.date, str]
        :param http_status_code: HTTP status code of the request
        :type http_status_code: int
        :param number_of_lightnings: Number of lightnings obtained from the Meteocat API call
        :type number_of_lightnings:
        """
        if type(date) is str:
            self.date = dateutil.parser.isoparse(date).replace(minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)
        else:
            self.date = date.replace(minute=0, second=0, microsecond=0, tzinfo=pytz.UTC)
        self.http_status_code = http_status_code
        self.number_of_lightnings = number_of_lightnings
