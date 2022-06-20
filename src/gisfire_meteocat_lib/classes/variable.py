#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations  # Needed to allow returning type of enclosing class PEP 563

import enum
import datetime
import json

from . import Base
from .state import State
from sqlalchemy import Enum
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from typing import Union
from typing import Dict
from typing import Optional
from typing import Any


class VariableCategory(str, enum.Enum):
    """
    Defines thr three types of variables

    DAT for real measured data
    AUX for auxiliary data
    CMV for compound multivariate data that is calculated
    """
    DAT = 'DAT'
    AUX = 'AUX'
    CMV = 'CMV'


class VariableStateCategory(enum.Enum):
    """
    Defines the three types of states for a variable

    DISMANTLED for dismantled stations
    ACTIVE for active station
    REPAIR for station under some type of repair or temporal inactivity
    """
    DISMANTLED = 1
    ACTIVE = 2
    REPAIR = 3


class VariableTimeBaseCategory(str, enum.Enum):
    """
    Defines the different types of sampling times for a variable
    """
    HO = 'HO'
    SH = 'SH'
    DM = 'DM'
    MI = 'MI'
    D5 = 'D5'


class VariableState(State):
    """
    Class container for the variable state table. Provides the SQL Alchemy access to the different states of a
    variable. A variable state informs of the presence of a certain variable measure in a specific weather station

    The Variable state is part of a ternary relation with a Variable and a Station.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio

    :type __tablename__: str
    :type code: VariableStateCategory or Column or None
    :type ts: datetime.datetime or Column
    """
    __tablename__ = 'meteocat_variable_state'
    code = Column('_codi', Enum(VariableStateCategory), nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    # assoc = relationship('WeatherStationVariableStateAssociation', back_populates='state', lazy='dynamic')

    def __init__(self, code: Optional[VariableStateCategory, None] = None,
                 from_date: Optional[datetime.datetime, None] = None,
                 to_date: Optional[datetime.datetime, None] = None) -> None:
        """
        Variable State constructor

        :param code: Variable state type
        :type code: VariableStateCategory
        :param from_date: Start date of validity od the variable state
        :type from_date: datetime
        :param to_date: Finishing date of the validity of the variable state
        :type to_date: datetime
        """
        super().__init__(from_date=from_date, to_date=to_date)
        self.code = code

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> VariableState:
        """
        Decodes a JSON originated dict from the Meteocat API to a VariableState object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: VariableState
        """
        state = VariableState()
        state.code = VariableStateCategory(dct['codi'])
        State.object_hook_abstract(dct, state)
        return state

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a database VariableState to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Lightning data

            :param obj:
            :type obj: VariableState
            :return: dict
            """
            if isinstance(obj, VariableState):
                obj: VariableState
                dct_variable_state = dict()
                dct_variable_state['code'] = int(obj.code.value)
                dct_state = State.JSONEncoder().default(obj)
                # Merges the two dicts with values from dct_weather_station_state replacing those from dct_state
                return {**dct_state, **dct_variable_state}
            return json.JSONEncoder.default(self, obj)  # pragma: no cover


class VariableTimeBase(State):
    """
    Class container for the variable time bases table. Provides the SQL Alchemy access to the different measurement
    intervals of a certain variable in a specific weather station. The different time intervals can be hourly,
    semi-hourly (30 min.), etc.

    The Variable time base is part of a ternary relation with a Variable and a Station.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio

    :type __tablename__: str
    :type code: VariableStateCategory or Column or None
    :type ts: datetime.datetime or Column
    """
    __tablename__ = 'meteocat_variable_time_base'
    code = Column('_codi', Enum(VariableTimeBaseCategory), nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    # assoc_variable_time_base = relationship('WeatherStationVariableTimeBaseAssociation', back_populates='time_base', lazy='dynamic')

    def __init__(self, code: Optional[VariableTimeBaseCategory, None] = None,
                 from_date: Optional[datetime.datetime, None] = None,
                 to_date: Optional[datetime.datetime, None] = None) -> None:
        """
        Variable time base object constructor
        :param code: Variable time base type
        :type code: VariableTimeBaseCategory
        :param from_date: Start date of validity od the variable time base
        :type from_date: datetime
        :param to_date: Finishing date of the validity of the variable time base
        :type to_date: datetime
        """
        super().__init__(from_date, to_date)
        self.code = code

    def __eq__(self, other: VariableTimeBase) -> bool:
        """
        Equality comparator

        :param other: The other time base to compare with
        :type other: VariableTimeBase
        """
        if isinstance(other, VariableTimeBase):
            return super().__eq__(other) and (self.code == other.code)
        else:
            return False  # pragma: no cover

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> VariableTimeBase:
        """
        Decodes a JSON originated dict from the Meteocat API to a VariableTimeBase object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: Dict[str, Any]
        :return: VariableTimeBase
        """
        time_base = VariableTimeBase()
        time_base.code = VariableTimeBaseCategory(dct['codi'])
        State.object_hook_abstract(dct, time_base)
        return time_base

    class JSONEncoder(json.JSONEncoder):
        """
        JSON Encoder to convert a database VariableTimeBase to JSON
        """

        def default(self, obj: object) -> Dict[str, Any]:
            """
            Default procedure to create a dictionary with the Variable time bas2 data

            :param obj:
            :type obj: Lightning
            :return: dict
            """
            if isinstance(obj, VariableTimeBase):
                obj: VariableTimeBase
                dct_variable_time_base = dict()
                dct_variable_time_base['code'] = str(obj.code.value)
                dct_state = State.JSONEncoder().default(obj)
                # Merges the two dicts with values from dct_weather_station_state replacing those from dct_state
                return {**dct_state, **dct_variable_time_base}
            return json.JSONEncoder.default(self, obj)  # pragma: no cover


class Variable(Base):
    """
    Class container for the variable table.  Provides the SQL Alchemy access to the different variables that can be
    measured or calculated in the different weather stations.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-totes-les-variables

    :type __tablename__: str
    :type id: int
    :type code: int
    :type unit: str
    :type acronym: str
    :type category: VariableCategory
    :type decimal_positions: int
    :type measures: relationship
    :type states: list()
    :type time_bases: list()
    """
    __tablename__ = 'meteocat_variable'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', Integer, nullable=False, unique=True)
    name = Column('_nom', String, nullable=False)
    unit = Column('_unitat', String, nullable=False)
    acronym = Column('_acronim', String, nullable=False)
    category = Column('_tipus', Enum(VariableCategory), nullable=False)
    decimal_positions = Column('_decimals', Integer, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    measures = relationship('Measure', back_populates='variable')
    # TODO: Add weather station relationship

    def __init__(self, code: Optional[int, None] = None, name: Optional[str, None] = None,
                 unit: Optional[str, None] = None, acronym: Optional[str, None] = None,
                 category: Optional[VariableCategory, None] = None,
                 decimal_positions: Optional[int, None] = None) -> None:
        """
        Variable constructor

        :param code: MeteoCat code of the variable in its API
        :type code: int
        :param name: Name of the variable in the MeteoCat API
        :type name: str
        :param unit: Units of measure of the variable
        :type unit: str
        :param acronym: Acronym of the variable
        :type acronym: str
        :param category: Variable type. Can be DAT (real measured DATa), AUX (Auxiliary data) or CMV (Compound
        MultiVariate)
        :type category: VariableCategory
        :param decimal_positions: Number of significant decimals of the measures
        :type decimal_positions: int
        """
        self.code = code
        self.name = name
        self.unit = unit
        self.acronym = acronym
        self.category = category
        self.decimal_positions = decimal_positions
        self.states = list()
        self.time_bases = list()

    @staticmethod
    def object_hook(dct: Dict[str, Any]) -> Union[Variable, Dict[str, Any], None]:
        """
        Decodes a JSON originated dict from the Meteocat API to a Lightning object

        :param dct: Dictionary with the standard parsing of the json library
        :type dct: dict
        :return: Variable
        """
        # weather station state dict of the Meteocat API JSON
        if all(k in dct for k in ('codi', 'dataInici', 'dataFi')):
            if isinstance(dct['codi'], str):
                time_base = VariableTimeBase.object_hook(dct)
                return time_base
            else:
                state = VariableState.object_hook(dct)
                return state
        if not (all(k in dct for k in ('codi', 'nom', 'unitat', 'acronim', 'tipus', 'decimals', 'basesTemporals'))):
            return None
        variable = Variable()
        variable.code = int(dct['codi'])
        variable.name = str(dct['nom'])
        variable.unit = str(dct['unitat'])
        variable.acronym = str(dct['acronim'])
        variable.category = VariableCategory(str(dct['tipus']))
        variable.decimal_positions = int(dct['decimals'])
        if variable.category != VariableCategory.CMV:
            if 'estats' not in dct:
                return None
            for state in dct['estats']:
                state: VariableState
                variable.states.append(state)
        else:
            variable.states = None
        for time_base in dct['basesTemporals']:
            time_base: VariableTimeBase
            if time_base not in variable.time_bases:
                variable.time_bases.append(time_base)
        return variable

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
            if isinstance(obj, Variable):
                obj: Variable
                dct = dict()
                dct['code'] = obj.code
                dct['name'] = obj.name
                dct['category'] = obj.category.value
                dct['unit'] = obj.unit
                dct['acronym'] = obj.acronym
                dct['decimal_positions'] = obj.decimal_positions
                dct['states'] = [VariableState.JSONEncoder().default(state) for state in obj.states]
                dct['time_bases'] = [VariableTimeBase.JSONEncoder().default(time_base) for time_base in obj.time_bases]
                return dct
            return json.JSONEncoder.default(self, obj)  # pragma: no cover
