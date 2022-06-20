#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

from . import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

from .variable import VariableTimeBaseCategory
from .weather_station import WeatherStation

import enum
import datetime
import dateutil.parser
import json

from typing import Optional
from typing import Dict
from typing import Any
from typing import Union
from typing import List


class MeasureValidityCategory(str, enum.Enum):
    """
    Defines the three types of measure validity
    """
    PENDING = ' '
    VALID = 'V'
    VALIDATING = 'T'


class MeasureTimeBaseCategory(str, enum.Enum):
    """
    Defines the different types of sampling times for a variable
    """
    HO = 'HO'
    SH = 'SH'


class Measure(Base):
    """
    Class container for measures table.  It provides SQL Alchemy access to the measures read from the weather stations

    :type __tablename__: str
    :type id: int
    :type date: datetime
    :type value: float
    :type validity_state: MeasureState
    :type time_base: VariableTimeBaseCategory
    :type meteocat_weather_station_id: int
    :type meteocat_variable_id: int
    :type ts: datetime
    :type station: relationship
    :type variable: relationship
   """
    __tablename__ = 'meteocat_measure'
    id = Column(Integer, primary_key=True)
    meteocat_id = Column('_meteocat_id', String, nullable=False)
    date = Column('_data', DateTime(timezone=True), nullable=False)
    date_extreme = Column('_data_extrem', DateTime(timezone=True))
    value = Column('_valor', Float, nullable=False)
    validity_state = Column('_estat', Enum(MeasureValidityCategory), nullable=False)
    time_base = Column('_base_horaria', Enum(MeasureValidityCategory), nullable=False)
    meteocat_weather_station_id = Column(Integer, ForeignKey('meteocat_weather_station.id'))
    meteocat_variable_id = Column(Integer, ForeignKey('meteocat_variable.id'))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    station = relationship('WeatherStation', back_populates='measures', foreign_keys=[meteocat_weather_station_id])
    variable = relationship('Variable', back_populates='measures', foreign_keys=[meteocat_variable_id])

    def __init__(self, meteocat_id: Optional[str, None] = None,
                 date: Optional[datetime.datetime, None] = None,
                 date_extreme: Optional[datetime.datetime, None] = None,
                 value: Optional[float, None] = None,
                 validity_state: Optional[MeasureValidityCategory, None] = None,
                 time_base: Optional[VariableTimeBaseCategory, None] = None) -> None:
        """
        Class constructor

        :param meteocat_id: Possible ID of the MeteoCat weather agency
        :type meteocat_id: str
        :param date: Date of the measure
        :type date: datetime.datetime
        :param date_extreme: Date of the extreme measure recorded
        :type date_extreme: datetime.datetime
        :param value: Value of the measure
        :type value: float
        :param validity_state: Validation state. The data read can have different validation stages (pending,
        validating or validated)
        :type validity_state: MeasureValidityCategory
        :param time_base: Data sampling period. The period can be every hour (HO) or every 30 min. (SH)
        :type time_base: MeasureTimeBaseCategory
        """
        self.meteocat_id = meteocat_id
        self.date = date
        self.date_extreme = date_extreme
        self.value = value
        self.validity_state = validity_state
        self.time_base = time_base

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> Union[List[Measure], Dict[str, Any], None]:
        """
        Decodes a JSON originated dict from the Meteocat API to a Measure object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict(str, Any)
        :return: Lightning
        """
        # 'data', 'valor', 'estat', 'baseHoraria' dict of the Meteocat API JSON
        if all(k in dct for k in ('data', 'valor', 'estat', 'baseHoraria')):
            return dct
        if not (all(k in dct for k in ('codi', 'lectures'))):
            return None
        measures = list()
        for measure_reading in dct['lectures']:
            measure = Measure()
            measure.date = dateutil.parser.isoparse(measure_reading['data'])
            measure.value = measure_reading['valor']
            measure.validity_state = MeasureValidityCategory(measure_reading['estat'])
            measure.time_base = MeasureTimeBaseCategory(measure_reading['baseHoraria'])
            measures.append(measure)
        return measures

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a Measure object to JSON string
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Measure data

            :param obj:
            :type obj: object
            :return: dict
            """
            if isinstance(obj, Measure):
                obj: Measure
                dct = dict()
                dct['value'] = obj.value
                dct['date'] = obj.date.strftime("%Y-%m-%dT%H:%MZ")
                dct['validity_state'] = obj.validity_state.value
                dct['time_base'] = obj.time_base.value
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover

    class GeoJSONEncoder(json.JSONEncoder):
        """
        Geo JSON Encoder to convert a Measure object to a GeoJSON string
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: object
            :return: dict
            """
            if isinstance(obj, Measure):
                obj: Measure
                dct: Dict[str, Any] = dict()
                if obj.station is None:
                    dct['error'] = 'No Weather Station linked with the Measure'
                else:
                    # noinspection DuplicatedCode
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
                    dct['geometry']['coordinates'] = [obj.station.lon, obj.station.lat]
                    dct['properties'] = Measure.JSONEncoder().default(obj)
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
