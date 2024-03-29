#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import enum
import datetime
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
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import Union
from typing import Dict
from typing import Optional
from typing import Any
from typing import List

from meteocat.data_model.state import State


class WeatherStationCategory(enum.Enum):
    """
    Defines the type of weather station

    AUTO for automatic weather stations
    OTHER for types different from automatic
    """
    AUTO = 0
    OTHER = 1


class WeatherStationStateCategory(enum.Enum):
    """
    Defines the three types os statuses

    DISMANTLED for dismantled stations
    ACTIVE for active station
    REPAIR for station under some type of repair or temporal inactivity
    """
    ACTIVE = 2
    DISMANTLED = 1
    REPAIR = 3


class WeatherStationState(State):
    """
    Class container for the weather station status table.  Provides the SQL Alchemy access to the different status of
    the timeline of a weather station. A weather station status informs of the presence of a certain weather station in
    the system.

    The weather station status information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/metadades-estacions/#metadades-de-totes-les-estacions

    :type __tablename__: str
    :type code: WeatherStationStateCategory or Column or None
    :type weather_station_id: int or Column
    :type ts: datetime.datetime or Column
    :type station: relationship
    """
    __tablename__ = 'weather_station_state'
    code = mapped_column('_codi', Enum(WeatherStationStateCategory, name='weather_station_state_category'), nullable=False)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    weather_station_id = Column(Integer, ForeignKey('weather_station.id'))
    station: Mapped["WeatherStation"] = relationship(back_populates='states')

    def __init__(self, code: Optional[WeatherStationStateCategory] = None,
                 from_date: Optional[datetime.datetime, None] = None,
                 to_date: Optional[datetime.datetime, None] = None) -> None:
        super().__init__(from_date, to_date)
        self.code = code

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> WeatherStationState:
        """
        Decodes a JSON originated dict from the Meteocat API to a WeatherStationStatus object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: WeatherStationStatus
        """
        status = WeatherStationState()
        status.code = WeatherStationStateCategory(dct['codi'])
        State.object_hook_abstract(dct, status)
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
            if isinstance(obj, WeatherStationState):
                obj: WeatherStationState
                dct_weather_station_state = dict()
                dct_weather_station_state['code'] = int(obj.code.value)
                dct_state = State.JSONEncoder().default(obj)
                # Merges the two dicts with values from dct_weather_station_state replacing those from dct_state
                return {**dct_state, **dct_weather_station_state}
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
    :type postgis_geometry = str or Column
    :type states: relationship
    :type measures: relationship
    :type SRID_WEATHER_STATIONS: int
    """
    SRID_WEATHER_STATIONS = 4258
    __tablename__ = 'weather_station'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code = mapped_column('_codi', String, nullable=False, unique=True)
    name = mapped_column('_nom', String, nullable=False)
    category = mapped_column('_tipus', Enum(WeatherStationCategory, name='weather_station_category'), nullable=False)
    _coordinates_latitude = mapped_column('_coordenades_latitud', Float, nullable=False)
    _coordinates_longitude = mapped_column('_coordenades_longitud', Float, nullable=False)
    placement = mapped_column('_emplacament', String, nullable=False)
    altitude = mapped_column('_altitud', Float, nullable=False)
    municipality_code = mapped_column('_municipi_codi', Integer, nullable=False)
    municipality_name = mapped_column('_municipi_nom', String, nullable=False)
    county_code = mapped_column('_comarca_codi', Integer, nullable=False)
    county_name = mapped_column('_comarca_nom', String, nullable=False)
    province_code = mapped_column('_provincia_codi', Integer, nullable=False)
    province_name = mapped_column('_provincia_nom', String, nullable=False)
    network_code = mapped_column('_xarxa_codi', Integer, nullable=False)
    network_name = mapped_column('_xarxa_nom', String, nullable=False)
    ts: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    postgis_geometry = mapped_column('geom', Geometry(geometry_type='POINT', srid=SRID_WEATHER_STATIONS))
    states: Mapped[List["WeatherStationState"]] = relationship("WeatherStationState", back_populates='station', lazy='joined')
    measures = relationship("Measure", back_populates='station', lazy='select')
    # TODO: add variables relationship

    def __init__(self, code: Optional[str, None] = None, name: Optional[str, None] = None,
                 category: Optional[WeatherStationCategory, None] = None,
                 coordinates_latitude: Optional[float, None] = None,
                 coordinates_longitude: Optional[float, None] = None, placement: Optional[str, None] = None,
                 altitude: Optional[float, None] = None, municipality_code: Optional[int, None] = None,
                 municipality_name: Optional[str, None] = None, county_code: Optional[int, None] = None,
                 county_name: Optional[str, None] = None, province_code: Optional[int, None] = None,
                 province_name: Optional[str, None] = None, network_code: Optional[int, None] = None,
                 network_name: Optional[str, None] = None) -> None:
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
        super().__init__()
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
            self.postgis_geometry = "SRID={2:};POINT({0:} {1:})".format(self._coordinates_longitude, self._coordinates_latitude,
                                                                        self.SRID_WEATHER_STATIONS)
        else:
            self.postgis_geometry = None

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
    def object_hook(dct: Dict[str, Any]) -> Union[WeatherStation, Dict[str, Any], WeatherStationState, None]:
        """
        Decodes a JSON originated dict from the Meteocat API to a Lightning object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict
        :return: Lightning
        """
        # 'municipi', 'comarca', 'provincia' or 'xarxa' dict of the Meteocat API JSON
        if all(k in dct for k in ('codi', 'nom')) and len(dct) == 2:
            return dct
        # weather station status dict of the Meteocat API JSON
        if all(k in dct for k in ('codi', 'dataInici', 'dataFi')):
            state = WeatherStationState.object_hook(dct)
            return state
        # Lat-lon coordinates dict of the Meteocat API JSON
        if all(k in dct for k in ('latitud', 'longitud')):
            return dct
        if not (all(k in dct for k in ('codi', 'nom', 'tipus', 'coordenades', 'emplacament', 'altitud', 'municipi',
                                       'comarca', 'provincia', 'xarxa', 'estats'))):
            return None
        station = WeatherStation()
        station.code = str(dct['codi'])
        station.name = str(dct['nom'])
        station.category = WeatherStationCategory.AUTO if str(dct['tipus']) == 'A' else WeatherStationCategory.OTHER
        station.placement = str(dct['emplacament'])
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
        for state in dct['estats']:
            state: WeatherStationState
            station.states.append(state)
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
                dct['category'] = obj.category.value
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
                dct['states'] = [WeatherStationState.JSONEncoder().default(state) for state in obj.states]
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover

    class GeoJSONEncoder(json.JSONEncoder):
        """
        Geo JSON Encoder to convert a database weather station to JSON
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
                dct['crs']['properties']['href'] = 'https://spatialreference.org/ref/epsg/' + \
                                                   str(WeatherStation.SRID_WEATHER_STATIONS) + '/proj4/'
                dct['crs']['properties']['type'] = 'proj4'
                dct['geometry'] = dict()
                dct['geometry']['type'] = 'Point'
                dct['geometry']['coordinates'] = [obj._coordinates_longitude, obj._coordinates_latitude]
                dct['properties'] = WeatherStation.JSONEncoder().default(obj)
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
