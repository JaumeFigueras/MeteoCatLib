#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum

from sqlalchemy import Enum
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class VariableCategory(enum.Enum):
    """
    Defines thr three types of variables

    DAT for real measured data
    AUX for auxiliary data
    CMV for compound multivariate data that is calculated
    """
    DAT = 0
    AUX = 1
    CMV = 2


class VariableStatus(Base):
    """
    Class container for the variable status table.  Provides the SQL Alchemy access to the different status of a
    variable. A variable status informs of the presence of a certain variable measure in a specific weather station

    The Variable status is part of a ternary relation with a Variable and a Station.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio

    TODO
    """
    __tablename__ = 'meteocat_variable_status'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', Integer, nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, code, from_date, to_date=None):
        self.code = code
        self.from_date = from_date
        self.to_date = to_date


class VariableTimeBasis(Base):
    """
    Class container for the variable time bases table. Provides the SQL Alchemy access to the different measurement
    intervals of a certain variable in a specific weather station. The different time intervals can be hourly,
    semi-hourly (30 min.), etc.

    The Variable time basis is part of a ternary relation with a Variable and a Station.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio

    TODO
    """
    __tablename__ = 'meteocat_variable_time_basis'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False)
    from_date = Column('_data_inici', DateTime(timezone=True), nullable=False)
    to_date = Column('_data_fi', DateTime(timezone=True))
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)

    def __init__(self, code, from_date, to_date=None):
        self.code = code
        self.from_date = from_date
        self.to_date = to_date


class Variable(Base):
    """
    Class container for the variable table.  Provides the SQL Alchemy access to the different variables that can be
    measured or calculated in the different weather stations.

    The variable information is obtained from the MeteoCat API call described in:
    https://apidocs.meteocat.gencat.cat/documentacio/dades-mesurades/#metadades-de-les-variables-duna-estacio

    :type id: int
    :type code: str
    :type unit: str
    :type acronym: str
    :type category: VariableCategory
    :type decimals: int
    :type measures: relationship
    """
    __tablename__ = 'meteocat_variable'
    id = Column(Integer, primary_key=True)
    code = Column('_codi', String, nullable=False, unique=True)
    name = Column('_nom', String, nullable=False)
    unit = Column('_unitat', String, nullable=False)
    acronym = Column('_acronim', String, nullable=False)
    category = Column('_tipus', Enum(VariableCategory), nullable=False)
    decimals = Column('_decimals', String, nullable=False)
    ts = Column(DateTime(timezone=True), server_default=func.utcnow(), nullable=False)
    measures = relationship('Measure', back_populates='variable')

    def __init__(self, code, name, unit, acronym, category, decimals):
        """
        Variable constructor

        :param code: MeteoCat code of the variable in its API
        :type code: str
        :param name: Name of the variable in the MeteoCat API
        :type name: str
        :param unit: Units of measure of the variable
        :type unit: str
        :param acronym: Acronym of the variable
        :type acronym: str
        :param category: Variable type. Can be DAT (real measured DATa), AUX (AUXiliary data) or CMV (Compound
        MultiVariate)
        :type category: VariableCategory
        :param decimals: Number of significant decimals of the measures
        :type decimals: int
        """
        self.code = code
        self.name = name
        self.unit = unit
        self.acronym = acronym
        self.category = category
        self.decimals = decimals




