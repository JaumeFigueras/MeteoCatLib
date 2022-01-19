#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import enum
import datetime
import dateutil.parser
import json

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import func
from sqlalchemy import ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship

from typing import Union
from typing import Dict
from typing import Optional
from typing import Any


class WeatherStationCategory(enum.Enum):
    """
    Defines the type of weather station

    AUTO for automatic weather stations
    OTHER for types different from automatic
    """
    AUTO = 0
    OTHER = 1


class WeatherStationStatusCategory(enum.Enum):
    """
    Defines the three types os statuses

    DISMANTLED for dismantled stations
    ACTIVE for active station
    REPAIR for station under some type of repair or temporal inactivity
    """
    ACTIVE = 1
    DISMANTLED = 2
    REPAIR = 3


class WeatherStationStatus(Base):
    """
    Class container for the weather station status table.  Provides the SQL Alchemy access to the different status of
    the timeline of a weather station. A weather station status informs of the presence of a certain weather station in
    the system.

    The weather station status information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/metadades-estacions/#metadades-de-totes-les-estacions

    :type __tablename__: str
    :type id: int or Column
    :type code: WeatherStationStatusCategory or Column or None
    :type from_date: datetime.datetime or Column or None
    :type to_date: datetime.datetime or Column or None
    :type meteocat_weather_station_id: int or Column
    :type ts: datetime.datetime or Column
    :type station: relationship
    """
    __tablename__ = 'meteocat_weather_station_status'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', Enum(WeatherStationStatusCategory), nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='status')

    def __init__(self, code: Optional[WeatherStationStatusCategory, None] = None,
                 from_date: Optional[datetime.datetime, None] = None,
                 to_date: Optional[datetime.datetime, None] = None) -> None:
        self.code = code
        self.from_date = from_date
        self.to_date = to_date

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> WeatherStationStatus:
        """
        Decodes a JSON originated dict from the Meteocat API to a WeatherStationStatus object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: WeatherStationStatus
        """
        status = WeatherStationStatus()
        status.code = WeatherStationStatusCategory(dct['codi'])
        try:
            status.from_date = dateutil.parser.isoparse(dct['dataInici'])
        except ValueError as e:
            raise e
        if dct['dataFi'] is None:
            status.to_date = None
        else:
            try:
                status.to_date = dateutil.parser.isoparse(dct['dataFi'])
            except ValueError as e:
                raise e
        return status

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a database WeatherStationStatus to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: Lightning
            :return: dict
            """
            if isinstance(obj, WeatherStationStatus):
                obj: WeatherStationStatus
                dct = dict()
                dct['code'] = int(obj.code.value)
                dct['from_date'] = obj.from_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                dct['to_date'] = obj.to_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover


class WeatherStation(Base):
    """
    Class container for the weather station table.  Provides the SQL Alchemy access to the different weather stations.

    The weather station information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/metadades-estacions/#metadades-de-totes-les-estacions

    :type __tablename__: str
    :type id: int
    :type code: str
    :type name: str
    :type category: WeatherStationCategory
    :type _coordinates_latitude: float
    :type _coordinates_longitude: float
    :type placement: str
    :type altitude: float
    :type municipality_code: int
    :type municipality_name: str
    :type county_code: int
    :type county_name: str
    :type province_code: int
    :type province_name: str
    :type network_code: int
    :type network_name: str
    :type ts: datetime
    :type __geom = str or Column
    :type status: relationship
    :type measures: relationship
    :type SRID_WEATHER_STATIONS: int
    """
    SRID_WEATHER_STATIONS = 4258
    __tablename__ = 'meteocat_weather_station'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False, unique=True)
    name = Column('_nom', String, nullable=False)
    category = Column('_tipus', Enum(WeatherStationCategory), nullable=False)
    _coordinates_latitude = Column('_coordenades_latitud', Float, nullable=False)
    _coordinates_longitude = Column('_coordenades_longitud', Float, nullable=False)
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
    __geom = Column(Geometry(geometry_type='POINT', srid=SRID_WEATHER_STATIONS))
    status = relationship("WeatherStationStatus", back_populates='station', lazy='joined')
    # TODO: Finish the relation
    # measures = relationship("Measure", back_populates='station', lazy='select')

    def __init__(self, code: Union[str, None] = None, name: Union[str, None] = None, 
                 category: Union[WeatherStationCategory, None] = None, coordinates_latitude: Union[float, None] = None,
                 coordinates_longitude: Union[float, None] = None, placement: Union[str, None] = None, 
                 altitude: Union[float, None] = None, municipality_code: Union[int, None] = None, 
                 municipality_name: Union[str, None] = None, county_code: Union[int, None] = None, 
                 county_name: Union[str, None] = None, province_code: Union[int, None] = None, 
                 province_name: Union[str, None] = None, network_code: Union[int, None] = None, 
                 network_name: Union[str, None] = None) -> None:
        """

        :param code: Station code provided by the Meteocat API
        :type code: str
        :param name: Station name
        :type name: str
        :param category: Type of the station
        :type category: WeatherStationCategory
        :param coordinates_latitude: Latitude of the location of the weather station
        :type coordinates_latitude: float
        :param coordinates_longitude: Longitude of the location of the weather station
        :type coordinates_longitude: float
        :param placement: Description of the location of the station
        :type placement: str
        :param altitude: Altitude above the sea level of the station
        :type altitude: float
        :param municipality_code: Spanish INE municipality code of the station location
        :type municipality_code: int
        :param municipality_name: Name of the municipality where the station is located
        :type municipality_name: str
        :param county_code: Spanish INE county code of the station location
        :type county_code: int
        :param county_name: Name of the county where the station is located
        :type county_name: str
        :param province_code: Spanish INE province code of the station location
        :type province_code: int
        :param province_name: Name of the province where the station is located
        :type province_name: str
        :param network_code: Code of the network where the station belongs
        :type network_code: int
        :param network_name: Name of the network where the station belongs
        :type network_name: str
        """
        self.code = code
        self.name = name
        self.category = category
        self._coordinates_latitude = coordinates_latitude
        self._coordinates_longitude = coordinates_longitude
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
        self.__format_geom()

    def __format_geom(self) -> None:
        """
        Unique procedure to convert the member attributes coordinate_latitude and coordinate longitude to a OSGeo WKT
        standard format

        :return: None
        """
        if (self._coordinates_latitude is not None) and (self._coordinates_longitude is not None):
            self.__geom = "SRID={2:};POINT({0:} {1:})".format(self._coordinates_longitude, self._coordinates_latitude,
                                                              self.SRID_WEATHER_STATIONS)
        else:
            self.__geom = None

    @property
    def geom(self) -> str:
        """
        Latitude getter

        :return: Lightning latitude
        :rtype: float
        """
        return self.__geom

    @property
    def lat(self) -> float:
        """
        Latitude getter

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
        Longitude getter

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

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> Union[WeatherStation, Dict[str, Any], None]:
        """
        Decodes a JSON originated dict from the Meteocat API to a Lightning object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict
        :return: Lightning
        """
        # 'municipi', 'comarca', 'provincia' or 'xarxa' dict of the Meteocat API JSON
        if all(k in dct for k in ('codi', 'nom')):
            return dct
        # weather station status dict of the Meteocat API JSON
        if all(k in dct for k in ('codi', 'dataInici', 'dataFi')):
            status = WeatherStationStatus.object_hook(dct)
            return status
        # Lat-lon coordinates dict of the Meteocat API JSON
        if all(k in dct for k in ('latitud', 'longitud')):
            return dct
        if not (all(k in dct for k in ('id', 'data', 'correntPic', 'chi2', 'ellipse', 'numSensors', 'nuvolTerra',
                                       'coordenades'))):
            return None
        station = WeatherStation()
        station.code = str(dct['codi'])
        station.name = str(dct['name'])
        station.category = WeatherStationCategory.AUTO if str(dict['tipus']) == 'A' else WeatherStationCategory.OTHER
        station.placement = str(dict['emplacament'])
        station.altitude = float(dct['altitud'])
        station._coordinates_latitude = float(dct['coordenades']['latitud'])
        station._coordinates_longitude = float(dct['coordenades']['longitud'])
        station.municipality_code = int(dct['municipi']['codi'])
        station.municipality_name = str(dct['municipi']['nom'])
        station.county_code = int(dct['comarca']['codi'])
        station.county_name = str(dct['comarca']['nom'])
        station.province_code = int(dct['provincia']['codi'])
        station.province_name = str(dct['provincia']['nom'])
        station.network_code = int(dct['xarxa']['codi'])
        station.network_name = str(dct['xarxa']['nom'])
        station.__format_geom()
        return station

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a database lightning to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: object
            :return: dict
            """
            if isinstance(obj, WeatherStation):
                obj: WeatherStation
                dct = dict()
                dct['code'] = obj.code
                dct['name'] = obj.name
                dct['category'] = obj.category
                dct['placement'] = obj.placement
                dct['altitude'] = obj.altitude
                dct['coordinates_latitude'] = obj._coordinates_latitude
                dct['coordinates_longitude'] = obj._coordinates_longitude
                dct['coordinates_epsg'] = WeatherStation.SRID_WEATHER_STATIONS
                dct['municipality_code'] = obj.municipality_code
                dct['municipality_name'] = obj.municipality_name
                dct['county_code'] = obj.county_code
                dct['county_name'] = obj.county_name
                dct['province_code'] = obj.province_code
                dct['province_name'] = obj.province_name
                dct['network_code'] = obj.network_code
                dct['network_name'] = obj.network_name
                dct['status'] = [WeatherStationStatus.JSONEncoder().default(state) for state in obj.status]
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover

    class GeoJSONEncoder(json.JSONEncoder):
        """
        Geo JSON Encoder to convert a database lightning to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: object
            :return: dict
            """
            if isinstance(obj, WeatherStation):
                obj: WeatherStation
                dct = dict()
                dct['type'] = 'Feature'
                dct['id'] = obj.id
                dct['crs'] = dict()
                dct['crs']['type'] = 'link'
                dct['crs']['properties'] = dict()
                dct['crs']['properties']['href'] = 'https://spatialreference.org/ref/epsg/4258/proj4/'
                dct['crs']['properties']['type'] = 'proj4'
                dct['geometry'] = dict()
                dct['geometry']['type'] = 'Point'
                dct['geometry']['coordinates'] = '[' + str(obj._coordinates_longitude) + ' ' + \
                                                 str(obj._coordinates_latitude) + ']'
                dct['properties'] = WeatherStation.JSONEncoder().default(obj)
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
